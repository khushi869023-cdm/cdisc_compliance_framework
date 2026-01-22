from loader import load_csv, load_json
from validator import (
    check_required_columns,
    check_min_value,
    check_allowed_values
)

df = load_csv("data/sdtm/dm.csv")
rules = load_json("rules/sdtm/dm_rules.json")

errors = []
errors += check_required_columns(df, rules["required_columns"])
errors += check_min_value(df, "AGE", rules["constraints"]["AGE"]["min"])
errors += check_allowed_values(df, "SEX", rules["constraints"]["SEX"]["allowed_values"])

for e in errors:
    print(e)

