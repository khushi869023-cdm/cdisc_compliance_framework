# CDISC Compliance Framework

A lightweight, rule-driven framework for validating clinical trial data against CDISC standards.

## Current Scope
- SDTM domain: DM (Demographics)
- External rule configuration via JSON
- CSV-based clinical data validation
- Clear, human-readable validation output

## Project Structure
├── data/<BR>
│ └── sdtm/<br>
│ └── dm.csv<br>
├── rules/<br>
│ └── sdtm/<br>
│ └── dm_rules.json<br>
├── src/<br>
│ ├── loader.py<br>
│ ├── validator.py<br>
│ └── run.py<br>
├── requirements.txt<br>
└── README.md<br>


## How It Works
1. Clinical data is loaded from CSV files.
2. Validation rules are defined externally in JSON.
3. A generic validation engine checks structure and values.
4. Errors are reported with row and column context.

## How to Run
```bash
pip install -r requirements.txt
python src/run.py


## sample output 
Row 3, Column 'AGE': Missing required value
Row 4, Column 'AGE': Value -5 < minimum 0
Row 5, Column 'SEX': Invalid value 'X'
