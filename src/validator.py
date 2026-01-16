import pandas as pd


class ValidationError:
    def __init__(self, row, column, message):
        self.row = row
        self.column = column
        self.message = message

    def __str__(self):
        if self.row is None:
            return f"{self.column}: {self.message}"
        return f"Row {self.row}, Column '{self.column}': {self.message}"


def check_required_columns(df: pd.DataFrame, required_columns: list):
    errors = []
    for col in required_columns:
        if col not in df.columns:
            errors.append(ValidationError(None, col, "Missing required column"))
    return errors


def check_min_value(df: pd.DataFrame, column: str, min_value: float):
    errors = []
    for idx, value in df[column].items():
        if pd.isna(value):
            errors.append(
                ValidationError(idx + 1, column, "Missing required value")
            )
        elif value < min_value:
            errors.append(
                ValidationError(
                    idx + 1, column, f"Value {value} < minimum {min_value}"
                )
            )
    return errors


def check_allowed_values(df: pd.DataFrame, column: str, allowed_values: list):
    errors = []
    for idx, value in df[column].items():
        if pd.isna(value):
            continue
        if value not in allowed_values:
            errors.append(
                ValidationError(
                    idx + 1, column, f"Invalid value '{value}'"
                )
            )
    return errors
