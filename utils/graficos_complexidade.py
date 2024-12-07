import plotly.graph_objects as go

def gerar_graficos_complexidade():
    # Dados da complexidade temporal (valores teóricos aproximados)
    algorithms = ['Round Robin', 'SJF', 'MLQ']
    time_complexity = [1, 2, 3]  # Escala arbitrária: O(n) -> 1, O(n log n) -> 2, O(m * n) -> 3

    # Dados da complexidade de implementação (escala arbitrária)
    implementation_complexity = [1, 2, 3]  # Fácil -> 1, Moderada -> 2, Alta -> 3

    # Gráfico para Complexidade Temporal
    fig_time = go.Figure()
    fig_time.add_trace(go.Bar(
        name='Complexidade Temporal',
        x=algorithms,
        y=time_complexity,
        marker_color=['red', 'green', 'blue']
    ))
    fig_time.update_layout(
        title='Complexidade Temporal dos Algoritmos',
        yaxis_title='Complexidade (Escala Arbitrária)',
        xaxis_title='Algoritmos'
    )

    # Gráfico para Complexidade de Implementação
    fig_implementation = go.Figure()
    fig_implementation.add_trace(go.Bar(
        name='Complexidade de Implementação',
        x=algorithms,
        y=implementation_complexity,
        marker_color=['orange', 'purple', 'cyan']
    ))
    fig_implementation.update_layout(
        title='Complexidade de Implementação dos Algoritmos',
        yaxis_title='Complexidade (Escala Arbitrária)',
        xaxis_title='Algoritmos'
    )

    # Mostrar os gráficos
    fig_time.show()
    fig_implementation.show()
