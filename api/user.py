from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from models.user import User
from utils.password import hash_password

# Créez un routeur FastAPI
user_router = APIRouter()


# Modèle Pydantic pour la création de compte
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True  # Anciennement `orm_mode = True`


# Route pour créer un compte
@user_router.post("/register/")
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'utilisateur existe déjà
    db_user = db.query(User).filter_by(username=user_create.username).first()
    if db_user:
        raise HTTPException(status_code=400,
                            detail="Username already registered")

    # Hacher le mot de passe
    hashed_password = hash_password(user_create.password)

    # Créer un nouvel utilisateur
    db_user = User(
        username=user_create.username,
        email=user_create.email,
        password_hash=hashed_password,
        first_name=user_create.first_name,
        last_name=user_create.last_name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created successfully"}
