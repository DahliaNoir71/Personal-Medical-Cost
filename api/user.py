from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from models.user import User
from utils.password import hash_password

# Créez un routeur FastAPI
user = APIRouter()


# Modèle Pydantic pour la création de compte
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_active: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True  # Anciennement `orm_mode = True`


# Route pour créer un compte
@user.post("/register/")
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'utilisateur existe déjà
    db_user = db.query(User).filter_by(username=user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # Hacher le mot de passe
    hashed_password = hash_password(user.password)

    # Créer un nouvel utilisateur
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}
