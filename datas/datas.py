import os
import pandas as pd

from faker import Faker


def load_datas_from_csv(file_path):
    # Validate the file path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    df = pd.read_csv(file_path)
    return df

def generate_names_based_on_sex(df, sex_column='sex', first_name_column='first_name', last_name_column='last_name'):
    """
    Génère des prénoms et des noms en fonction de la colonne 'sex' dans un DataFrame.

    :param df: DataFrame contenant la colonne 'sex'.
    :param sex_column: Nom de la colonne contenant le sexe ('male' ou 'female').
    :param first_name_column: Nom de la colonne pour les prénoms.
    :param last_name_column: Nom de la colonne pour les noms.
    :return: DataFrame avec les colonnes 'first_name' et 'last_name' remplies.
    """
    fake = Faker()

    # Générer des prénoms et des noms en fonction du sexe
    df[first_name_column] = df[sex_column].apply(
        lambda x: fake.first_name_male() if x == 'male' else fake.first_name_female()
    )
    df[last_name_column] = df[sex_column].apply(lambda x: fake.last_name())

    return df
