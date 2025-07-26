# rules/validate_hours.py

import pandas as pd

def validate(df):
    """
    Applies timesheet rules to the DataFrame and returns a list of violations.

    Rules:
    - More than 8 hours in a day
    - Work logged on weekend
    - Missing entries for workdays (Mon–Fri)
    """
    violations = []

    # Ensure date is datetime
    df['date'] = pd.to_datetime(df['date'])

    # Group by employee and date
    grouped = df.groupby(['employee_id', 'date']).agg({'hours_worked': 'sum'}).reset_index()

    for _, row in grouped.iterrows():
        eid = row['employee_id']
        date = row['date']
        hours = row['hours_worked']

        # Rule 1: More than 8 hours
        if hours > 8:
            violations.append({
                'employee_id': eid,
                'date': str(date.date()),
                'violation': f'Worked {hours} hours (> 8)'
            })

        # Rule 2: Weekend work
        if date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            violations.append({
                'employee_id': eid,
                'date': str(date.date()),
                'violation': 'Worked on weekend'
            })

    # Rule 3: Missing weekday entries
    all_employees = df['employee_id'].unique()
    all_dates = pd.to_datetime(df['date']).dt.date.unique()

    # Generate list of weekdays only
    weekdays = sorted(set(d for d in all_dates if pd.Timestamp(d).weekday() < 5))

    for eid in all_employees:
        employee_dates = set(df[df['employee_id'] == eid]['date'].dt.date)

        for day in weekdays:
            if day not in employee_dates:
                violations.append({
                    'employee_id': eid,
                    'date': str(day),
                    'violation': 'Missing timesheet entry for workday'
                })

    return violations
