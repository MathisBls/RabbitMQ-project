import subprocess
import sys
import os

# Utilise le bon interpréteur automatiquement (python3 sur Mac, python sur Windows)
python_cmd = sys.executable

# Chemins vers les scripts workers
workers = [
    os.path.join("workers", "worker_add.py"),
    os.path.join("workers", "worker_sub.py"),
    os.path.join("workers", "worker_mul.py"),
    os.path.join("workers", "worker_div.py")
]

processes = []

for worker in workers:
    p = subprocess.Popen([python_cmd, worker])
    processes.append(p)

try:
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    for p in processes:
        p.terminate()
