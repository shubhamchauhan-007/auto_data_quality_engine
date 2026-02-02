import pandas as pd 


def load_data(file_path):

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")