from pwdlib import PasswordHash

passwd_hash = PasswordHash.recommended()


def verify_password(plain_password, hashed_password):
    return passwd_hash.verify(plain_password, hashed_password)


def get_passwd_hash(plain_passwd):
    return passwd_hash.hash(plain_passwd)
