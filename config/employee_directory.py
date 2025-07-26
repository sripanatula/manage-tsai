# config/employee_directory.py

employee_profiles = {
    "E001": {
        "name": "Amina Yusuf",         # Nigeria
        "email": "amina_yusuf@mailinator.com",
        "phone": "+14251234567",       # Your mobile
        "notification_prefs": ["email", "sms"]
    },
    "E002": {
        "name": "Lucas Moretti",       # Brazil
        "email": "lucas.moretti@mailinator.com",
        "phone": "+12061234567",       # Google Voice
        "notification_prefs": ["sms", "email"]
    },
    "E003": {
        "name": "Mei Lin",             # China
        "email": "mei.lin@mailinator.com",
        "phone": "+12141234567",       # Virtual #1
        "notification_prefs": ["email"]
    },
    "E004": {
        "name": "Carlos Alvarez",      # Mexico
        "email": "carlos.alvarez@mailinator.com",
        "phone": "+19721234567",       # Virtual #2
        "notification_prefs": ["voice", "sms"]
    },
    "E005": {
        "name": "Sophie Dubois",       # France
        "email": "sophie.dubois@mailinator.com",
        "phone": "+1XXXXXXXX05",       # Optional 5th contact
        "notification_prefs": ["sms"]
    }
}

def get_profile(employee_id):
    return employee_profiles.get(employee_id, {})
