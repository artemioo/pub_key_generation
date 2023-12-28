from models import User
import coincurve.keys


def generate_keys(address, db):
    PrivKey = coincurve.PrivateKey()
    PublKey = coincurve.PublicKey.from_secret(PrivKey.secret)
    result = PublKey.format()
    user = User(address=address, public_key=result)
    db.add(user)
    db.commit()
    return user
