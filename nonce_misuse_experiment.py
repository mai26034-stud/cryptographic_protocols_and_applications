import os
from aes_gcm_cipher import AESGcmCipher
from chacha20_poly1305_cipher import ChaChaPolyCipher
from experimental_evaluation import benchmark

def misuse_test(cipher_class):
    key = cipher_class.generate_key()
    cipher = cipher_class(key)

    nonce = b'\x00' * cipher_class.NONCE_SIZE
    aad = b"aad"

    m1 = b"Secret message one"
    m2 = b"Secret message two"

    c1 = cipher.encrypt(nonce, aad, m1)
    c2 = cipher.encrypt(nonce, aad, m2)

    ct1 = c1[:-16]
    ct2 = c2[:-16]
    xor_ct = bytes(a ^ b for a, b in zip(ct1, ct2))
    xor_pt = bytes(a ^ b for a, b in zip(m1, m2))

    print(f"{cipher_class.__name__} nonce reuse test:")
    print(f"Plaintext XOR : {xor_pt}")
    print(f"Ciphertext XOR: {xor_ct}")
    print(f"Keystream leak? {'YES' if xor_ct == xor_pt else 'NO'}\n")

if __name__ == "__main__":
    import json
    from aes_gcm_cipher import AESGcmCipher
    from chacha20_poly1305_cipher import ChaChaPolyCipher

    print("Running benchmarks for AES-GCM...")
    aes_results = benchmark(AESGcmCipher)
    print("\nRunning benchmarks for ChaCha20-Poly1305...")
    chacha_results = benchmark(ChaChaPolyCipher)

    print("\n=== AES-GCM Results ===")
    for r in aes_results:
        print(f"Size: {r['size']} bytes | Throughput: {r['throughput_mb_s']:.2f} MB/s | Latency: {r['latency_ms']:.4f} ms")

    print("\n=== ChaCha20-Poly1305 Results ===")
    for r in chacha_results:
        print(f"Size: {r['size']} bytes | Throughput: {r['throughput_mb_s']:.2f} MB/s | Latency: {r['latency_ms']:.4f} ms")

    with open("aes_gcm_benchmark.json", "w") as f:
        json.dump(aes_results, f, indent=2)
    with open("chacha_benchmark.json", "w") as f:
        json.dump(chacha_results, f, indent=2)

    print("\nResults saved to JSON files for plotting.")
