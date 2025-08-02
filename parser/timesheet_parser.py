# parser/timesheet_parser.py

import pandas as pd
import os
from logger import log_info, log_error, log_debug

def parse_timesheet(file_path):
    """
    Parses a timesheet from CSV or Excel and returns a pandas DataFrame.

    Supports:
    - .csv (comma-separated)
    - .xlsx (Excel)

    Expected columns: employee_id, date, hours_worked
    """
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".csv":
            df = pd.read_csv(file_path)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Use .csv or .xlsx.")

        # Basic validation (for debugging or early failure)
        required_cols = {"employee_id", "date", "hours_worked"}
        if not required_cols.issubset(df.columns):
            missing = required_cols - set(df.columns)
            raise ValueError(f"Missing required columns: {', '.join(missing)}")

        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])

        log_info("Timesheet parsed successfully", {
            "file_path": file_path,
            "rows": len(df),
            "columns": list(df.columns)
        })

        return df

    except Exception as e:
        log_error("Failed to parse timesheet", {
            "file_path": file_path,
            "error": str(e)
        })
        raise
