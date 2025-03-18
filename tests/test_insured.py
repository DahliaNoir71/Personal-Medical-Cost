import pytest
from sqlalchemy.exc import IntegrityError

from models.insured import Insured


# Test CREATE
def test_create_insured(db_session):
    # Créer un nouvel assuré
    insured = Insured(
        first_name="John",
        last_name="Doe",
        age=30,
        sex="Male",
        bmi=22.5,
        children=2,
        smoker="No",
        region="Northwest",
        charges=1000.0,
    )
    db_session.add(insured)
    db_session.commit()

    # Vérifier que l'assuré a été ajouté
    assert insured.id is not None
    assert insured.first_name == "John"
    assert insured.last_name == "Doe"


# Test READ
def test_read_insured(db_session):
    # Ajouter un assuré pour le test
    insured = Insured(
        first_name="Jane",
        last_name="Smith",
        age=25,
        sex="Female",
        bmi=20.0,
        children=0,
        smoker="No",
        region="Southeast",
        charges=500.0,
    )
    db_session.add(insured)
    db_session.commit()

    # Récupérer l'assuré depuis la base de données
    retrieved_insured = (db_session.query(Insured)
                         .filter_by(first_name="Jane").first())

    # Vérifier les données
    assert retrieved_insured is not None
    assert retrieved_insured.last_name == "Smith"
    assert retrieved_insured.age == 25


# Test UPDATE
def test_update_insured(db_session):
    # Ajouter un assuré pour le test
    insured = Insured(
        first_name="Alice",
        last_name="Johnson",
        age=40,
        sex="Female",
        bmi=30.0,
        children=3,
        smoker="Yes",
        region="Northeast",
        charges=2000.0,
    )
    db_session.add(insured)
    db_session.commit()

    # Modifier l'assuré
    insured.age = 41
    insured.charges = 2100.0
    db_session.commit()

    # Récupérer l'assuré mis à jour
    updated_insured = (db_session.query(Insured)
                       .filter_by(first_name="Alice").first())

    # Vérifier les modifications
    assert updated_insured.age == 41
    assert updated_insured.charges == 2100.0


# Test DELETE
def test_delete_insured(db_session):
    # Ajouter un assuré pour le test
    insured = Insured(
        first_name="Bob",
        last_name="Brown",
        age=50,
        sex="Male",
        bmi=25.0,
        children=1,
        smoker="No",
        region="Southwest",
        charges=1500.0,
    )
    db_session.add(insured)
    db_session.commit()

    # Supprimer l'assuré
    db_session.delete(insured)
    db_session.commit()

    # Vérifier que l'assuré a été supprimé
    deleted_insured = (db_session.query(Insured)
                       .filter_by(first_name="Bob").first())
    assert deleted_insured is None


# Test contrainte NOT NULL
def test_not_null_constraint(db_session):
    # Tentative de création d'un assuré avec un champ manquant
    with pytest.raises(IntegrityError):
        insured = Insured(
            first_name=None,  # Champ obligatoire manquant
            last_name="Doe",
            age=30,
            sex="Male",
            bmi=22.5,
            children=2,
            smoker="No",
            region="Northwest",
            charges=1000.0,
        )
        db_session.add(insured)
        db_session.commit()
