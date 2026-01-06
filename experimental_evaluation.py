import os
import time
import psutil

MESSAGE_SIZES = [
    64, 256, 1024, 4096, 16384,
    65536, 262144, 1048576,
    4194304, 16777216, 67108864
]

REPETITIONS = {
    size: 10000 if size <= 4096 else
          1000 if size <= 1048576 else
          100
    for size in MESSAGE_SIZES
}

def benchmark(cipher_class):
    results = []
    process = psutil.Process()

    for size in MESSAGE_SIZES:
        message = os.urandom(size)
        aad = b"associated_data"
        key = cipher_class.generate_key()
        cipher = cipher_class(key)

        for _ in range(5):
            cipher.encrypt(os.urandom(cipher_class.NONCE_SIZE), aad, message)

        cpu_before = process.cpu_percent()
        memory_before = process.memory_info().rss

        start = time.perf_counter_ns()
        for _ in range(REPETITIONS[size]):
            nonce = os.urandom(cipher_class.NONCE_SIZE)
            ct = cipher.encrypt(nonce, aad, message)
            cipher.decrypt(nonce, aad, ct)
        elapsed_ns = time.perf_counter_ns() - start

        cpu_after = process.cpu_percent()
        memory_after = process.memory_info().rss

        ops = REPETITIONS[size] * 2
        throughput = (size * ops) / (elapsed_ns / 1e9) / 1e6
        latency = (elapsed_ns / 1e9 * 1000) / REPETITIONS[size]

        results.append({
            "size": size,
            "throughput_mb_s": throughput,
            "latency_ms": latency,
            "cpu_usage_percent": (cpu_before + cpu_after) / 2,
            "memory_peak_mb": max(memory_before, memory_after) / 1e6
        })

    return results
