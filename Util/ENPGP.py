import pgpy

key, _ = pgpy.PGPKey.from_file("id_rsa.pub")
skey, _ = pgpy.PGPKey.from_file("id_rsa")

def new_key():
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)


def encode(msg):
    msg1 = pgpy.PGPMessage.new(msg)
    encrypted_message = key.encrypt(msg1)
    print("cipher:")
    print(msg1)
    print(encrypted_message)


def decode(msg):
    msg1 = pgpy.PGPMessage.new(msg)
    decrypted_message = skey.decrypt(msg1)
    print("cipher:")
    print(msg1)
    print(decrypted_message)
