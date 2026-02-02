def apply_rules(profile: dict, schema: dict):

    issues = []

    for column, rules in schema.get("columns", {}).items():
        if column not in profile["columns"]:
            issues.append({
                "column": column,
                "issue": "missing_column"
            })
            continue
        
        col_profile = profile["columns"][column]

        if rules.get("required") and col_profile["missing_count"] > 0:
            issues.append({
                "column": column,
                "issue": "missing_required_values",
                "count": col_profile["missing_count"]
            })

        if rules.get("unique") and col_profile["unique_count"] < profile["row_count"]:
            issues.append({
                "column": column,
                "issue": "duplicate_values"
            })

    return issues