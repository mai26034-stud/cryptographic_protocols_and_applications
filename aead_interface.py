from abc import ABC, abstractmethod

class AeadCipher(ABC):
    KEY_SIZE: int
    NONCE_SIZE: int

    @staticmethod
    @abstractmethod
    def generate_key() -> bytes:
        pass

    @abstractmethod
    def encrypt(self, nonce: bytes, aad: bytes, plaintext: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, nonce: bytes, aad: bytes, ciphertext: bytes) -> bytes:
        pass
