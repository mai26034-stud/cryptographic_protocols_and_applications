This repository contains the Python implementation and experimental code
used in the postgraduate course assignment:

**Course:** Cryptographic Protocols and Applications  
**Title:** Comparative study and experimental evaluation of the AEAD algorithms
AES-GCM and ChaCha20-Poly1305  
Student: Alexandros Kyriakidis mai26034

The purpose of this repository is to support the experimental evaluation
presented in the written assignment. The code implements a common AEAD
interface and provides:

- An implementation of AES-GCM using the `cryptography` library
- An implementation of ChaCha20-Poly1305 using the `PyNaCl` library
- Benchmark scripts for throughput, latency, CPU and memory usage
- Experiments demonstrating the impact of nonce misuse

The code is intended exclusively for educational and research purposes
and not for production use.


## Repository Structure
- `aes_gcm_implementation.py`  
  Implementation of the AES-GCM AEAD scheme using the `cryptography` library.

- `chacha20_poly1305_implementation.py`  
  Implementation of the ChaCha20-Poly1305 AEAD scheme using the `PyNaCl` library.

- `experimental_evaluation.py`  
  Script used for the experimental evaluation of throughput, latency,
  CPU usage and memory consumption.

- `nonce_misuse_experiment.py`  
  Script demonstrating the behavior of the two AEAD schemes in the case
  of nonce reuse.


Requirements:
- Python 3.11+
- cryptography
- PyNaCl
- psutil
- matplotlib

Dependencies can be installed using:

```bash
pip install -r requirements.txt
