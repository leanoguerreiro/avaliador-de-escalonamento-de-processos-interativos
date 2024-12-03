import random
from Process import Process

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
        arrival = random.randint(0, 10)  # Tempo de chegada entre 0 e 10
        burst = random.randint(1, 10)    # Tempo de burst entre 1 e 10
        priority = random.choice(['high', 'low'])  # Prioridade aleatória
        processes.append(Process(i, arrival, burst, priority))
    return processes
