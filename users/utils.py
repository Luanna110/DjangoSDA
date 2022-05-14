import hashlib

def hash_password_without_salt(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode('ascii')).hexdigest()
    return hashed_password
