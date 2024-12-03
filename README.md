# Avaliador de Escalonamento de Processos Interativos

Este projeto implementa um avaliador para algoritmos de escalonamento de processos interativos. Ele inclui a implementação de três algoritmos clássicos de escalonamento: Round Robin (RR), Shortest Job First (SJF) e Múltiplas Filas (MLQ). O projeto também gera dados aleatórios para simular processos e utiliza gráficos interativos para visualizar o desempenho dos algoritmos.

## Estrutura do Projeto

- `main.py`: Arquivo principal que coordena a execução do projeto. Gera dados aleatórios, executa os algoritmos de escalonamento e exibe gráficos.
- `round_robin.py`: Implementação do algoritmo Round Robin.
- `shortest_job_first.py`: Implementação do algoritmo Shortest Job First.
- `multilevel_queue.py`: Implementação do algoritmo Múltiplas Filas.
- `data_generator.py`: Funções para gerar dados aleatórios, como processos, tempos de burst, prioridades e quantum.
- `requirements.txt`: Lista das dependências necessárias para executar o projeto.

## Avaliação dos Algoritmos

A avaliação dos algoritmos de escalonamento é feita através do cálculo de três métricas principais de desempenho:

1. **Tempo de Espera Médio**
   - **Definição:** Média do tempo que cada processo passa na fila de prontos antes de começar a ser executado.
   - **Uso:** Ajuda a avaliar quanto tempo, em média, os processos estão esperando antes de serem atendidos pela CPU. Menores tempos indicam melhor desempenho em termos de responsividade.

2. **Tempo de Turnaround Médio**
   - **Definição:** Média do tempo total desde a submissão de um processo até sua conclusão.
   - **Uso:** Indica a eficiência geral do sistema em processar tarefas. Um menor tempo de turnaround médio sugere que o sistema está processando as tarefas rapidamente.

3. **Throughput**
   - **Definição:** Número de processos concluídos por unidade de tempo.
   - **Uso:** Mostra a capacidade do sistema em lidar com cargas de trabalho. Um maior throughput indica que mais processos estão sendo completados em menos tempo.

## Dependências

O projeto requer as seguintes bibliotecas Python:

- NumPy
- Plotly

Estas dependências estão listadas no arquivo `requirements.txt`.

## Instalação

1. **Clone o Repositório:**
   ```bash
   [git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/leanoguerreiro/avaliador-de-escalonamento-de-processos-interativos.git)
   cd avaliador-de-escalonamento-de-processos-interativos
