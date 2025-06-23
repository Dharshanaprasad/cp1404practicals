"""Emails and Names
"""

def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    return " ".join(parts).title()

email_to_name = {}
email = input("Email: ")
while email != "":
    name = extract_name(email)
    confirmed = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmed not in ("", "y"):
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
