import pgpy
from pgpy.constants import PubKeyAlgorithm


def create(name, email, password):
    key, _ = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    return key


def encode(msg, key):
    msg1 = pgpy.PGPMessage.new(msg)
    encrypted_message = key.encrypt(msg1)
    return encrypted_message


def decode(msg, skey):
    with skey.unlock("C0rrectPassphr@se"):
        msg1 = pgpy.PGPMessage.new(msg)
        decrypted_message = skey.decrypt(msg1)
        return decrypted_message


def encode_file(file, key):
    with open(file, "r") as f:
        s = ""
        while True:
            line1 = f.readline()
            if line1:
                s += line1 + "\n"
            else:
                break
        msg = encode(s, key)
        return msg


def decode_file(file, skey):
    with skey.unlock("C0rrectPassphr@se"):
        with open(file, "r") as f:
            s = ""
            while True:
                line1 = f.readline()
                if line1:
                    s += line1 + "\n"
                else:
                    break
            msg = decode(s, skey)
            return msg
