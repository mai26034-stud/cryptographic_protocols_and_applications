import os
from aead.aes_gcm import AESGcmCipher
from aead.chacha20_poly1305 import ChaChaPolyCipher

def misuse_test(cipher_class):
    key = cipher_class.generate_key()
    cipher = cipher_class(key)

    nonce = os.urandom(cipher_class.NONCE_SIZE)
    aad = b"aad"

    m1 = b"Secret message one"
    m2 = b"Secret message two"

    c1 = cipher.encrypt(nonce, aad, m1)
    c2 = cipher.encrypt(nonce, aad, m2)

    print(f"{cipher_class.__name__} nonce reuse test:")
    print("Ciphertext XOR:", bytes(a ^ b for a, b in zip(c1, c2)))

if __name__ == "__main__":
    misuse_test(AESGcmCipher)
    misuse_test(ChaChaPolyCipher)
