import json
import pandas as pd


def load_data():
    return pd.read_csv("dm.csv")


def load_rules():
    with open("dm_rules.json", "r") as f:
        return json.load(f)


def validate(df, rules):
    errors = []

    # required columns
    for col in rules["required_columns"]:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")

    # AGE checks
    for i, value in df["AGE"].items():
        if pd.isna(value):
            errors.append(f"Row {i+1}: AGE missing")
        elif value < rules["constraints"]["AGE"]["min"]:
            errors.append(f"Row {i+1}: AGE < 0")

    # SEX checks
    allowed_sex = rules["constraints"]["SEX"]["allowed_values"]
    for i, value in df["SEX"].items():
        if value not in allowed_sex:
            errors.append(f"Row {i+1}: Invalid SEX '{value}'")

    return errors


def main():
    df = load_data()
    rules = load_rules()
    errors = validate(df, rules)

    print("\nValidation Output")
    print("-" * 30)
    for e in errors:
        print(e)


if __name__ == "__main__":
    main()
