import pandas as pd
from engine.loader import load_data_in_chunks
from engine.cleaner import clean_data
from engine.profiler import profile_data
from engine.config_loader import load_schema



def run_pipeline(file_path, schema_path, output_path):
    schema = load_schema(schema_path)
    cleaned_chunks = []

    for chunk in load_data_in_chunks(file_path):
        cleaned_chunk = clean_data(chunk, schema)
        cleaned_chunks.append(cleaned_chunk)

    final_df = pd.concat(cleaned_chunks, ignore_index=True)
    final_df.to_csv(output_path, index=False)

    print("FINAL PROFITABLE:")
    print(profile_data(final_df))



if __name__ == "__main__":
    run_pipeline("data/incoming/sample.csv",
                  "config/schema.yaml",
                  "data/cleaned/cleaned_data.csv"
    )