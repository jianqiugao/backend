from passlib.context import CryptContext

_pwd_contex = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return _pwd_contex.verify(plain_password, hashed_password)


def get_password_hash(plain_password):
    return _pwd_contex.hash(plain_password)