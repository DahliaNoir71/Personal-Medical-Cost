import os
import pandas as pd


def load_datas_from_csv(file_path):
    # Validate the file path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    df = pd.read_csv(file_path)
    return df
