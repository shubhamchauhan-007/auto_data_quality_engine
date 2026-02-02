import pandas as pd 


def load_data_in_chunks(file_path, chunk_size=100_00):

    try:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            yield chunk
    except Exception as e:
        raise RuntimeError(f"Failed to load data in chunks: {e}")