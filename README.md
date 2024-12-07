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

1. **Tempo de Espera Médio**
   - **Descrição:** Média do tempo que cada processo passa na fila de prontos antes de começar a ser executado.
   - **Uso:** Mede a responsividade do sistema. Menores tempos indicam maior eficiência.
   - **Eixo X:** Algoritmos (Round Robin, SJF, MLQ).
   - **Eixo Y:** Tempo de Espera Médio (em milissegundos).

2. **Tempo de Turnaround Médio**
   - **Descrição:** Média do tempo total desde a submissão de um processo até sua conclusão.
   - **Uso:** Mede a eficiência geral do sistema em processar tarefas. Menores tempos indicam maior eficiência.
   - **Eixo X:** Algoritmos (Round Robin, SJF, MLQ).
   - **Eixo Y:** Tempo de Turnaround Médio (em milissegundos).

3. **Throughput**
   - **Descrição:** Número de processos concluídos por unidade de tempo.
   - **Uso:** Mede a capacidade do sistema em lidar com cargas de trabalho. Maiores valores indicam maior eficiência.
   - **Eixo X:** Algoritmos (Round Robin, SJF, MLQ).
   - **Eixo Y:** Throughput (processos por milissegundo).

### Visualização dos Gráficos

Os gráficos gerados permitem uma comparação clara entre os algoritmos com base nas métricas avaliadas:

#### 1. Gráfico do Tempo de Espera Médio
- Mostra o tempo médio que os processos aguardam antes de serem executados.
- Ajuda a identificar qual algoritmo é mais eficiente em reduzir o tempo de espera.

#### 2. Gráfico do Tempo de Turnaround Médio
- Mostra o tempo médio total que os processos levam desde a submissão até a conclusão.
- Permite avaliar a eficiência global do sistema.

#### 3. Gráfico do Throughput
- Mostra quantos processos são concluídos por unidade de tempo.
- Indica qual algoritmo é mais eficiente em lidar com cargas maiores.

### Resultado Esperado

Após executar o projeto, você verá três gráficos interativos:

1. **Gráfico do Tempo de Espera Médio:**
   - Compara os algoritmos em termos do tempo médio que os processos esperam na fila.

2. **Gráfico do Tempo de Turnaround Médio:**
   - Compara os algoritmos em termos do tempo total médio necessário para processar os processos.

3. **Gráfico do Throughput:**
   - Compara os algoritmos em termos da quantidade média de processos concluídos por unidade de tempo.

Esses gráficos ajudam a identificar qual algoritmo é mais adequado para diferentes cenários operacionais e permitem uma análise visual clara das diferenças entre eles.

### Observações

- As métricas são calculadas com base nos tempos simulados para cada processo gerado aleatoriamente.
- Os gráficos são gerados com Plotly, permitindo interatividade e visualizações dinâmicas.

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

## Análise dos Resultados dos Gráficos

Os gráficos gerados neste projeto apresentam uma análise comparativa entre os algoritmos de escalonamento (Round Robin, Shortest Job First e Múltiplas Filas) com base em métricas de desempenho e complexidade. A seguir, são descritos os principais resultados e suas implicações.

---

### **Gráficos de Desempenho**

#### 1. **Tempo de Espera Médio**
- **Descrição:** O gráfico do tempo de espera médio exibe a média do tempo que os processos aguardam na fila de prontos antes de serem executados.
- **Interpretação:**
  - Algoritmos com menor tempo de espera médio são mais responsivos, especialmente em sistemas interativos.
  - O **Shortest Job First (SJF)** tende a apresentar o menor tempo de espera médio, pois prioriza os processos mais curtos, reduzindo o impacto do tempo de espera acumulado.
  - O **Round Robin (RR)** pode apresentar maiores tempos de espera dependendo da escolha do quantum, já que processos podem ser interrompidos frequentemente.
  - O desempenho do **Múltiplas Filas (MLQ)** é altamente dependente da configuração das filas e das prioridades atribuídas aos processos.

#### 2. **Tempo de Turnaround Médio**
- **Descrição:** O gráfico do tempo de turnaround médio apresenta o tempo total desde a submissão até a conclusão dos processos.
- **Interpretação:**
  - Algoritmos que minimizam o tempo de turnaround médio são mais eficientes no processamento geral das tarefas.
  - O **SJF** geralmente apresenta o menor turnaround médio devido à sua estratégia de priorizar processos curtos.
  - O **RR** pode ter um maior turnaround médio devido ao overhead gerado pela troca frequente entre processos.
  - O desempenho do **MLQ** depende da estrutura das filas; processos em filas de baixa prioridade podem sofrer atrasos significativos.

#### 3. **Throughput**
- **Descrição:** O gráfico do throughput exibe a quantidade média de processos concluídos por unidade de tempo.
- **Interpretação:**
  - Um throughput elevado indica que o algoritmo é eficiente em lidar com altas cargas de trabalho.
  - O **SJF** frequentemente apresenta um bom throughput, pois conclui rapidamente processos curtos, liberando recursos para novos processos.
  - No caso do **RR**, o throughput pode ser reduzido se o quantum for muito pequeno, devido ao overhead associado à troca constante entre processos.
  - O throughput do **MLQ** varia conforme as políticas definidas para cada fila e as prioridades atribuídas aos processos.

---

### **Gráficos da Complexidade**

#### 4. **Complexidade Temporal**
- **Descrição:** Este gráfico compara os algoritmos com base na eficiência teórica em relação ao tempo necessário para processar os dados.
- **Interpretação:**
  - A complexidade temporal dos algoritmos é avaliada teoricamente:
    - O **RR** possui complexidade linear ($O(n)$), pois cada processo é tratado uma vez por iteração.
    - O **SJF** possui complexidade log-linear ($O(n \log n)$), devido à necessidade de ordenação dos tempos de burst para determinar o próximo processo a ser executado.
    - O **MLQ** possui complexidade proporcional ao número total de filas ($m$) e processos ($n$), resultando em $O(m \cdot n)$.
  - Algoritmos com menor complexidade temporal são mais adequados para sistemas com grandes volumes de dados ou cargas intensas.

#### 5. **Complexidade de Implementação**
- **Descrição:** Este gráfico avalia a dificuldade relativa para implementar cada algoritmo.
- **Interpretação:**
  - A dificuldade é avaliada qualitativamente:
    - O **RR** é considerado fácil de implementar, pois utiliza uma fila circular simples para gerenciar os processos.
    - O **SJF** é moderadamente complexo, pois exige conhecimento prévio ou estimativa precisa dos tempos de burst e requer ordenação.
    - O **MLQ** apresenta alta complexidade devido à necessidade de gerenciar múltiplas filas com diferentes políticas e prioridades.

---

### Discussão Geral

#### Round Robin (RR)
- É um algoritmo simples e justo, adequado para sistemas interativos. Sua eficiência depende fortemente da escolha do quantum:
  - Quantums pequenos aumentam o overhead devido à troca constante entre processos.
  - Quantums grandes podem reduzir a responsividade.

#### Shortest Job First (SJF)
- É ideal para minimizar tempos médios (espera e turnaround), mas apresenta desafios práticos:
  - Requer conhecimento prévio ou estimativa precisa dos tempos de execução dos processos.
  - Pode levar à inanição (starvation) de processos longos se novos processos curtos continuarem chegando.

#### Múltiplas Filas (MLQ)
- É altamente flexível, permitindo lidar com diferentes tipos de cargas (foreground vs background). No entanto:
  - Sua eficiência depende da configuração das filas e das políticas associadas a cada nível.
  - Apresenta maior complexidade tanto na implementação quanto no gerenciamento.

---

### Conclusões Baseadas nos Gráficos

1. Para sistemas onde a responsividade é crítica, como sistemas interativos, o Round Robin pode ser uma boa escolha se configurado adequadamente (quantum balanceado).
2. Em cenários onde a eficiência global é prioritária e os tempos dos processos são conhecidos ou previsíveis, o SJF é a melhor opção devido ao seu baixo tempo médio de espera e turnaround.
3. Para sistemas que precisam lidar com diferentes tipos de cargas simultaneamente, como foreground e background, o MLQ oferece maior flexibilidade, embora seja mais complexo.

Os gráficos fornecem uma visão clara das diferenças entre os algoritmos em termos de desempenho e complexidade, auxiliando na escolha do algoritmo mais adequado para diferentes cenários operacionais.

---


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
