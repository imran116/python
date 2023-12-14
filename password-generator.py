import base64
import random
import string
import secrets

# Process One
smallAlpha = string.ascii_lowercase
capitalAlpha = string.ascii_uppercase
punctuation = string.punctuation
digit = string.digits

all_letters = smallAlpha + capitalAlpha + punctuation + digit

# password = ''.join(random.choices(all_letters, k=16))
password = ''.join((secrets.choice(all_letters) for _ in range(16)))  # we can also use secrets for more secure password

secure_token_base64 = base64.urlsafe_b64encode(secrets.token_bytes(16)).decode('utf-8')
print(secure_token_base64)
print(password)  # print 16 letters password


# Process Two


