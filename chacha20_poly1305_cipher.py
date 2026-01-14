import nacl.secret
import nacl.utils
from aead_interface import AeadCipher

class ChaChaPolyCipher(AeadCipher):
    KEY_SIZE = nacl.secret.SecretBox.KEY_SIZE
    NONCE_SIZE = nacl.secret.SecretBox.NONCE_SIZE

    def __init__(self, key: bytes):
        self.box = nacl.secret.SecretBox(key)

    @staticmethod
    def generate_key() -> bytes:
        return nacl.utils.random(ChaChaPolyCipher.KEY_SIZE)

    def encrypt(self, nonce: bytes, aad: bytes, plaintext: bytes) -> bytes:
        return self.box.encrypt(plaintext, nonce, aad)

    def decrypt(self, nonce: bytes, aad: bytes, ciphertext: bytes) -> bytes:
        return self.box.decrypt(ciphertext, nonce, aad)
