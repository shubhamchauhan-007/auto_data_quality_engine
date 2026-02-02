def profile_data(df):

    profile = {
        "row_count": len(df),
        "column_count":df.shape[1],
        "columns": {}
    }

    for column in df.columns:
        col_data = df[column]

        profile["columns"][column]={
            "dtype": str(col_data.dtype),
            "missing_count": int(col_data.isnull().sum()),
            "missing_percentage": round(col_data.isnull().mean() * 100, 2),
            "unique_count": int(col_data.nunique()),
        }

    profile["duplicate_rows"] = int(df.duplicated().sum())

    return profile