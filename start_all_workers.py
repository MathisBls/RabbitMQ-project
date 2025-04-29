import subprocess

workers = [
    "workers/worker_add.py",
    "workers/worker_sub.py",
    "workers/worker_mul.py",
    "workers/worker_div.py"
]

processes = []

for worker in workers:
    print(f"Lancement de {worker}...")
    p = subprocess.Popen(["python", worker])
    processes.append(p)

print("Tous les workers sont lancés. CTRL+C pour arrêter.")

for p in processes:
    p.wait()
