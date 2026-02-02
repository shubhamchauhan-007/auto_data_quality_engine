from engine.logger import logger

def clean_data(df, schema):

    for column, rules in schema.get("columns", {}).items():
        if column not in df.columns:
            continue

        actions = rules.get("action", {})

        if "missing" in actions:
            if actions["missing"] == "drop":
                before = len(df)
                df = df[df[column].notna()]
                after = len(df)

                logger.info(
                    f"Dropped {before - after} rows due to missing values in column: {column}"
                )

            elif actions["missing"] == "median":
                missing_count = df[column].isna().sum()
                df[column] = df[column].fillna(df[column].median())

                logger.info(
                    f"Filled {missing_count} missing values with median in column: {column}"
                )

            elif actions["missing"] == "mean":
                missing_count = df[column].isna().sum()
                df[column] = df[column].fillna(df[column].mean())

                logger.info(
                    f"Filled {missing_count} missing values with mean in column: {column}"
                )

            
        
        if "duplicates" in actions and actions["duplicates"] == "drop":
            before = len(df)
            df = df.drop_duplicates(subset=[column])
            after = len(df)

            logger.info(f"Dropped {before - after} duplicate rows based on column: {column}")

    return df
