from engine.loader import load_data
from engine.profiler import profile_data
# from engine.rule_engine import apply_rules
# from engine.cleaner import clean_data
# from engine.reporter import generate_report


def run_pipeline(file_path):
    df = load_data(file_path)

    profile = profile_data(df)

    print("DATA PROFILE:")
    for col, info in profile["columns"].items():
        print(f"{col}: {info}")

    print(f"Duplicate rows: {profile['duplicate_rows']}")

    # cleaning_plan = apply_rules(profile)

    # cleaned_df = clean_data(df, cleaning_plan)

    # generate_report(profile, cleaning_plan)

    # return cleaned_df

if __name__ == "__main__":
    run_pipeline("data/incoming/sample.csv")