from datas.datas import load_datas_from_csv, generate_names_based_on_sex


def main():
    df = load_datas_from_csv("csv/insurance.csv")
    df = generate_names_based_on_sex(df)
    print(df.head(10))

if __name__ == "__main__":
    main()
