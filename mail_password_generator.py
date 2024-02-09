import random
import string

def generate_email(name, id, domain):
    return f"{name.lower().replace(' ', '.')}.{id}@{domain}"

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    name = input("Enter your full name: ")
    user_id = input("Enter your user ID: ")
    domain = input("Enter your email domain: ")
    
    email = generate_email(name, user_id, domain)
    password = generate_password()


    print(f"Generated email: {email}")
    print(f"Generated password: {password}")
