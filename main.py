import numpy as np
import plotly.graph_objects as go
from algoritmos.round_robin import round_robin
from algoritmos.shortest_job_first import shortest_job_first
from algoritmos.multilevel_queue import multilevel_queue
from utils.data_generator import gerar_processos, gerar_burst_times, gerar_prioridades, gerar_quantum
from utils.analisys_complexity import gerar_graficos_complexidade

# Gerar dados aleatórios para os processos
num_processos = 150000
processos = gerar_processos(num_processos)
burst_times = gerar_burst_times(num_processos)
prioridades = gerar_prioridades(num_processos)
quantum = gerar_quantum()

# Executar algoritmos de escalonamento com os dados gerados
wt_rr, tat_rr = round_robin(processos, burst_times, quantum)
wt_sjf, tat_sjf = shortest_job_first(processos, burst_times)
wt_mlq, tat_mlq = multilevel_queue(processos, burst_times, prioridades)

# Calcular métricas de desempenho
metrics = {
    'Algoritmo': ['RR', 'SJF', 'MLQ'],
    'Tempo de Espera Médio': [
        np.mean(wt_rr), 
        np.mean(wt_sjf), 
        np.mean(wt_mlq)
    ],
    'Tempo de Turnaround Médio': [
        np.mean(tat_rr), 
        np.mean(tat_sjf), 
        np.mean(tat_mlq)
    ],
    'Throughput': [
        len(processos) / sum(tat_rr),
        len(processos) / sum(tat_sjf),
        len(processos) / sum(tat_mlq)
    ]
}

# Criar gráficos usando Plotly
fig_means = go.Figure()
fig_means.add_trace(go.Bar(
    name='Tempo de Espera Médio',
    x=metrics['Algoritmo'],
    y=metrics['Tempo de Espera Médio'],
    marker_color=['red', 'green', 'blue']
))
fig_means.update_layout(
    title='Tempo de Espera Médio por Algoritmo',
    yaxis_title='Tempo de Espera Médio (ms)'
)

fig_turnaround = go.Figure()
fig_turnaround.add_trace(go.Bar(
    name='Tempo de Turnaround Médio',
    x=metrics['Algoritmo'],
    y=metrics['Tempo de Turnaround Médio'],
    marker_color=['red', 'green', 'blue']
))
fig_turnaround.update_layout(
    title='Tempo de Turnaround Médio por Algoritmo',
    yaxis_title='Tempo de Turnaround Médio (ms)'
)

fig_throughput = go.Figure()
fig_throughput.add_trace(go.Bar(
    name='Throughput',
    x=metrics['Algoritmo'],
    y=metrics['Throughput'],
    marker_color=['red', 'green', 'blue']
))
fig_throughput.update_layout(
    title='Throughput por Algoritmo',
    yaxis_title='Throughput (processos/ms)'
)

# Mostrar gráficos Plotly
fig_means.show()
fig_turnaround.show()
fig_throughput.show()

# Gerar gráficos da complexidade dos algoritmos
gerar_graficos_complexidade()