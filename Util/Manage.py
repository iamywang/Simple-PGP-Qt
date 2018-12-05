import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm


def create(name, email, password):
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name, comment=name, email=email)
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
                ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
                compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP,
                             CompressionAlgorithm.Uncompressed])

    key.protect(password, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
    return key.pubkey


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
