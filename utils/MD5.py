import hashlib
from config.constans import SECRET_KEY


def md5(pwd):
    try:
        pwd = str(pwd)
    except Exception as E:
        return E
    obj = hashlib.md5(SECRET_KEY)
    obj.update(pwd.encode('utf-8'))
    return obj.hexdigest()
