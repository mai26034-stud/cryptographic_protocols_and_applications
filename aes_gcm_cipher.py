import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from aead_interface import AeadCipher

class AESGcmCipher(AeadCipher):
    KEY_SIZE = 32
    NONCE_SIZE = 12

    def __init__(self, key: bytes):
        self.aesgcm = AESGCM(key)

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(AESGcmCipher.KEY_SIZE)

    def encrypt(self, nonce: bytes, aad: bytes, plaintext: bytes) -> bytes:
        return self.aesgcm.encrypt(nonce, plaintext, aad)

    def decrypt(self, nonce: bytes, aad: bytes, ciphertext: bytes) -> bytes:
        return self.aesgcm.decrypt(nonce, ciphertext, aad)
