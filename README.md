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

  ## Avaliação do Grau de Complexidade dos Algoritmos

Além das métricas de desempenho (tempo de espera médio, tempo de turnaround médio e throughput), os algoritmos também são avaliados em relação à sua **complexidade computacional** e **facilidade de implementação**.

### 1. Round Robin (RR)

- **Complexidade de Tempo:**
  - A complexidade do Round Robin é \(O(n)\) por iteração, onde \(n\) é o número de processos. No pior caso, se todos os processos forem executados até o final do quantum, a complexidade total será proporcional ao número total de fatias de tempo necessárias para concluir todos os processos.
- **Complexidade de Implementação:**
  - Fácil de implementar, pois utiliza uma fila circular simples para gerenciar os processos.
- **Observações:**
  - O desempenho depende fortemente da escolha do quantum. Um quantum muito pequeno aumenta a troca de contexto (overhead), enquanto um quantum muito grande pode reduzir a capacidade de resposta do sistema.

### 2. Shortest Job First (SJF)

- **Complexidade de Tempo:**
  - A complexidade do SJF é \(O(n \log n)\), pois os tempos de burst precisam ser ordenados para selecionar o processo mais curto.
- **Complexidade de Implementação:**
  - Moderada, pois exige conhecimento prévio ou estimativa precisa dos tempos de execução dos processos, o que pode ser difícil em sistemas reais.
- **Observações:**
  - Embora minimize o tempo médio de espera, pode levar à inanição (starvation) se processos curtos continuarem chegando.

### 3. Múltiplas Filas (MLQ)

- **Complexidade de Tempo:**
  - Depende do número total de filas (\(m\)) e do número total de processos (\(n\)). No pior caso, cada fila pode ser percorrida para encontrar o próximo processo a ser executado, resultando em \(O(m \cdot n)\).
- **Complexidade de Implementação:**
  - Alta, pois envolve gerenciar múltiplas filas com diferentes níveis de prioridade e potencialmente diferentes algoritmos dentro de cada fila.
- **Observações:**
  - É flexível e pode ser ajustado para diferentes tipos de processos (foreground vs background), mas sua configuração correta pode ser desafiadora.

### Comparação Geral

| Algoritmo         | Complexidade Temporal | Complexidade de Implementação | Observações                                                                 |
|--------------------|------------------------|--------------------------------|-----------------------------------------------------------------------------|
| **Round Robin**    | \(O(n)\)              | Fácil                         | Simples e eficiente para sistemas time-sharing; depende da escolha do quantum. |
| **Shortest Job First** | \(O(n \log n)\)     | Moderada                      | Requer conhecimento prévio dos tempos; risco de inanição para processos longos. |
| **Múltiplas Filas** | \(O(m \cdot n)\)      | Alta                          | Flexível, mas complexo; ideal para sistemas com diferentes prioridades.        |


### Visualização dos Resultados

Os gráficos são gerados para comparar os algoritmos em termos de complexidade temporal e complexidade de implementação. Abaixo está uma descrição dos gráficos:

#### 1. Gráfico de Complexidade Temporal

- **Descrição:** Este gráfico compara os algoritmos com base na eficiência teórica do tempo necessário para processar os dados.
- **Eixo X:** Algoritmos (Round Robin, SJF, MLQ).
- **Eixo Y:** Complexidade Temporal (Escala Arbitrária).

#### 2. Gráfico de Complexidade de Implementação

- **Descrição:** Este gráfico avalia a dificuldade relativa de implementar cada algoritmo.
- **Eixo X:** Algoritmos (Round Robin, SJF, MLQ).
- **Eixo Y:** Complexidade de Implementação (Escala Arbitrária).

### Resultado Esperado

Após executar o projeto, você verá dois gráficos interativos:

1. **Gráfico de Complexidade Temporal:**
   - Mostra como cada algoritmo se comporta em termos da eficiência teórica do tempo necessário para processar os dados.

2. **Gráfico de Complexidade de Implementação:**
   - Compara a dificuldade relativa de implementar cada algoritmo.

Esses gráficos ajudam a entender as diferenças nos graus de complexidade dos algoritmos e fornecem uma visão visual clara das características teóricas e práticas.

### Observações

- A escala arbitrária usada nos gráficos é apenas para fins comparativos e pode ser ajustada conforme necessário.
- Os gráficos são gerados com a biblioteca Plotly, que permite interatividade e visualizações dinâmicas.

## Dependências

O projeto requer as seguintes bibliotecas Python:

- NumPy
- Plotly

Estas dependências estão listadas no arquivo `requirements.txt`.

## Instalação

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/leanoguerreiro/avaliador-de-escalonamento-de-processos-interativos.git
   cd avaliador-de-escalonamento-de-processos-interativos
2. **Crie um Ambiente Virtual(opicional, mas recomendado):**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # No Windows use: myenv\Scripts\activate
3. **Intalando as Dependências:**
   ```bash
   pip install -r requirements.txt

## Uso

Para executar o projeto, execute o script principal:
```bash
python3 main.py #ou apenas python ao invez de python3 no windows 
