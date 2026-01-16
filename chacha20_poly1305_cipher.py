import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from aead_interface import AeadCipher

class ChaChaPolyCipher(AeadCipher):
    KEY_SIZE = 32
    NONCE_SIZE = 12

    def __init__(self, key: bytes):
        if len(key) != self.KEY_SIZE:
            raise ValueError(f"Key must be {self.KEY_SIZE} bytes long")
        self.chacha = ChaCha20Poly1305(key)

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(ChaChaPolyCipher.KEY_SIZE)

    def encrypt(self, nonce: bytes, aad: bytes, plaintext: bytes) -> bytes:
        if len(nonce) != self.NONCE_SIZE:
            raise ValueError(f"Nonce must be {self.NONCE_SIZE} bytes long")
        return self.chacha.encrypt(nonce, plaintext, aad)

    def decrypt(self, nonce: bytes, aad: bytes, ciphertext: bytes) -> bytes:
        if len(nonce) != self.NONCE_SIZE:
            raise ValueError(f"Nonce must be {self.NONCE_SIZE} bytes long")
        return self.chacha.decrypt(nonce, ciphertext, aad)
