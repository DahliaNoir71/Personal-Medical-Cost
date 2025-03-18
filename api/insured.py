from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from models.insured import Insured

# Créez un routeur FastAPI
router = APIRouter()


class InsuredCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str
    charges: float


# Modèle Pydantic pour la réponse (lecture d'un assuré)
class InsuredResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str
    charges: float

    class Config:
        from_attributes = True  # Anciennement `orm_mode = True`


# CREATE : Ajouter un nouvel assuré
@router.post("/insured/", response_model=InsuredResponse)
def create_insured(insured: InsuredCreate, db: Session = Depends(get_db)):
    db_insured = Insured(**insured.model_dump())
    db.add(db_insured)
    db.commit()
    db.refresh(db_insured)
    return db_insured


# READ : Récupérer un assuré par ID
@router.get("/insured/{insured_id}", response_model=InsuredResponse)
def read_insured(insured_id: int, db: Session = Depends(get_db)):
    db_insured = db.query(Insured).filter_by(id=insured_id).first()
    if db_insured is None:
        raise HTTPException(status_code=404, detail="Assuré non trouvé")
    return db_insured


# READ ALL : Récupérer tous les assurés
@router.get("/insured/", response_model=list[InsuredResponse])
def read_all_insureds(db: Session = Depends(get_db)):
    return db.query(Insured).all()


# UPDATE : Mettre à jour un assuré
@router.put("/insured/{insured_id}", response_model=InsuredResponse)
def update_insured(insured_id: int, insured: InsuredCreate, db: Session = Depends(get_db)):
    db_insured = db.query(Insured).filter_by(id=insured_id).first()
    if db_insured is None:
        raise HTTPException(status_code=404, detail="Assuré non trouvé")

    for key, value in insured.model_dump().items():
        setattr(db_insured, key, value)

    db.commit()
    db.refresh(db_insured)
    return db_insured


# DELETE : Supprimer un assuré
@router.delete("/insured/{insured_id}", response_model=InsuredResponse)
def delete_insured(insured_id: int, db: Session = Depends(get_db)):
    db_insured = db.query(Insured).filter_by(id=insured_id).first()
    if db_insured is None:
        raise HTTPException(status_code=404, detail="Assuré non trouvé")

    db.delete(db_insured)
    db.commit()
    return db_insured
