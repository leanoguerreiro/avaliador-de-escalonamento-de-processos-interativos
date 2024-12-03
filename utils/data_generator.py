import random

def gerar_processos(n):
    return [f'P{i}' for i in range(1, n + 1)]

def gerar_burst_times(n, min_burst=1, max_burst=10):
    return [random.randint(min_burst, max_burst) for _ in range(n)]

def gerar_prioridades(n, min_priority=0, max_priority=5):
    return [random.randint(min_priority, max_priority) for _ in range(n)]

def gerar_quantum(min_quantum=1, max_quantum=5):
    return random.randint(min_quantum, max_quantum)
