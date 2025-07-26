from parser.timesheet_parser import parse_timesheet
from rules.validate_hours import validate
from notifier.notify import notify

import json
import sys

def log_violations(violations, path='logs/violations.json'):
    """
    Save all rule violations to a JSON file for audit or debug.
    """
    with open(path, 'w') as f:
        json.dump(violations, f, indent=2)


def main(file_path):
    """
    Main pipeline:
    1. Load timesheet
    2. Validate timesheet using rules
    3. Notify user about violations
    4. Log the violations to a file
    """
    df = parse_timesheet(file_path)
    violations = validate(df)

    for violation in violations:
       notify(violation)


    log_violations(violations)

# Step 4: Command-line interface support
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Usage: python main.py <path-to-timesheet-file>")
        sys.exit(1)
    main(sys.argv[1])