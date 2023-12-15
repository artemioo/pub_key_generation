from tinyec import registry
import secrets
from models import User
import hashlib


def generate_keys(address, db):
    curve = registry.get_curve('secp256r1')
    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g
    extended_pubKey = str(pubKey.x) + '.' + str(pubKey.y)
    hashed_key = hashlib.sha256(extended_pubKey.encode('utf-8')).hexdigest()
    user = User(address=address, public_key=hashed_key)
    db.add(user)
    db.commit()
    return user
