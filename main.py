import uvicorn
from fastapi import FastAPI

from api.insured import router as insured_router
from database.database import create_tables
from datas.datas import load_datas_from_csv, generate_names_based_on_sex
from modules.seed import seed_insured

app = FastAPI()
# Inclure le routeur avec le préfixe "/api"
app.include_router(insured_router, prefix="/api")


def main():
    df = load_datas_from_csv("csv/insurance.csv")
    df = generate_names_based_on_sex(df)
    print(df.head(10))
    create_tables()
    seed_insured(df)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
