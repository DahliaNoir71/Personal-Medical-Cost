import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Configuration de la base de données en mémoire pour les tests
@pytest.fixture(scope="module")
def db_session():
    Base = declarative_base()
    # Créer une base de données SQLite en mémoire
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Fournir la session aux tests

    # Nettoyer après les tests
    session.close()
    Base.metadata.drop_all(engine)
