import pandas as pd 

def infer_schema(df: pd.DataFrame) -> dict:

    schema = {"columns": {}}
    row_count = len(df)

    for column in df.columns:
        col = df[column]
        missing_pct = col.isna().mean()
        unique_pct = col.nunique() / row_count if row_count else 0

        inferred = {}

        if pd.api.types.is_integer_dtype(col):
            inferred["dtype"] = "int"

        elif pd.api.types.is_float_dtype(col):
            inferred["dtype"] = "float"

        elif pd.api.types.is_datetime64_any_dtype(col):
            inferred["dtype"] = "datetime"
        
        else:
            inferred["dtype"] = "string"

        
        inferred["required"] = missing_pct < 0.2

        if unique_pct > 0.95:
            inferred["unique"] = True

        inferred["action"] = {}

        if inferred["dtype"] in ["int", "float"]:
            inferred["action"]["missing"] = "median"
        
        else:
            inferred["action"]["missing"] = "drop"

        
        if inferred.get("unique"):
            inferred["action"]["duplicates"] = "drop"

        
        schema["columns"][column] = inferred

    
    return schema