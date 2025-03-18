from database.database import SessionLocal
from models.insured import Insured


def seed_insured(df):
    # Ouvrir une session de base de données
    db = SessionLocal()

    try:
        # Vérifier si la table est vide
        if db.query(Insured).count() == 0:
            # Insérer chaque ligne du DataFrame dans la base de données
            for _, row in df.iterrows():
                db_patient = Insured(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    age=row["age"],
                    sex=row["sex"],
                    bmi=row["bmi"],
                    children=row["children"],
                    smoker=row["smoker"],
                    region=row["region"],
                    charges=row["charges"],
                )
                db.add(db_patient)
            db.commit()
            print("Données insérées avec succès.")
        else:
            print("La table n'est pas vide. Aucune donnée n'a été insérée.")
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
        db.rollback()
    finally:
        db.close()
