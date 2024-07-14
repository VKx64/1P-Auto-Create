from datetime import datetime

def generate_email(email):
    formatted_time = datetime.now().strftime("%H%M%d")
    username, domain = email.split("@")
    formatted_email = f"{username}+{formatted_time}@{domain}"
    return formatted_email