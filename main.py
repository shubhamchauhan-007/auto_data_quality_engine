import os
import pandas as pd 

from engine.schema_infer import infer_schema
from engine.config_loader import load_schema
from engine.cleaner import clean_data
from engine.loader import load_data_in_chunks
from engine.profiler import profile_data



def run_pipeline(file_path, schema_path=None, output_path="data/cleaned/cleaned_data.csv"):

    chunk_iterator = load_data_in_chunks(file_path)

    first_chunk = next(chunk_iterator)

    if schema_path and os.path.exists(schema_path):
        schema = load_schema(schema_path)
        print("Using provided schema")

    else:
        schema = infer_schema(first_chunk)
        print("Schema inferred automatically")


    cleaned_chunks = []
    cleaned_first = clean_data(first_chunk, schema)
    cleaned_chunks.append(cleaned_first)


    for chunk in chunk_iterator:
        cleaned_chunk = clean_data(chunk, schema)
        cleaned_chunks.append(cleaned_chunk)


    final_df = pd.concat(cleaned_chunks, ignore_index=True)
    final_df.to_csv(output_path, index=False)

    print("FINAL PROFITABLE:")
    print(profile_data(final_df))



if __name__ == "__main__":
    run_pipeline("data/incoming/sample.csv",
                  schema_path=None,
                  output_path="data/cleaned/cleaned_data.csv"
    )