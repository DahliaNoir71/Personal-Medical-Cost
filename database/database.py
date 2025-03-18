from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.insured import Insured
from models.user import User


def create_tables():
    # Création des tables dans la base de données
    Insured.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# URL de la base de données SQLite
DATABASE_URL = "sqlite:///medical_costs.db"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session locale pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
