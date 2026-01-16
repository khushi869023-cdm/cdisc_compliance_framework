from loader import load_csv, load_json
from validator import (
    check_required_columns,
    check_min_value,
    check_allowed_values,
)


def main():
    df = load_csv("data/sdtm/dm.csv")
    rules = load_json("rules/sdtm/dm_rules.json")

    errors = []

    # structural checks
    errors += check_required_columns(df, rules["required_columns"])

    # AGE checks
    age_rules = rules["constraints"]["AGE"]
    errors += check_min_value(df, "AGE", age_rules["min"])

    # SEX checks
    sex_rules = rules["constraints"]["SEX"]
    errors += check_allowed_values(df, "SEX", sex_rules["allowed_values"])

    print("\nSDTM DM Validation Report")
    print("-" * 40)

    if not errors:
        print("No validation errors found.")
    else:
        for err in errors:
            print(err)


if __name__ == "__main__":
    main()

 