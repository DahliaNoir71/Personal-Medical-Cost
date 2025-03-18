from database.database import create_tables
from datas.datas import load_datas_from_csv, generate_names_based_on_sex
from modules.seed import seed_insured


def main():
    df = load_datas_from_csv("csv/insurance.csv")
    df = generate_names_based_on_sex(df)
    print(df.head(10))
    create_tables()
    seed_insured(df)


if __name__ == "__main__":
    main()
