from algoritmos.round_robin import round_robin
from algoritmos.shortest_job_first import shortest_job_first
from algoritmos.multilevel_queue import multilevel_queue
from utils.process_generator import generate_processes

def main():
    num_processes = 10
    
    # Gerar processos aleatórios.
    processes = generate_processes(num_processes)

    # Avaliar cada algoritmo com os processos gerados.
    rr_results = round_robin(processes[:], quantum=4)
    sjf_results = shortest_job_first(processes[:])
    mlq_results = multilevel_queue(processes[:])

    # Exibir resultados.
    print(f"Round Robin Results: {rr_results}")
    print(f"SJF Results: {sjf_results}")
    print(f"MLQ Results: {mlq_results}")

if __name__ == "__main__":
    main()

    # Execute testes com diferentes números e configurações de processos
  
    for i in range(5):
        print(f"\n=== Test Run {i+1} ===")
        
        # Gerar processos aleatórios
        processes = generate_processes(10)
        
        # Exibir processos gerados
        print("\nGenerated Processes:")
        for process in processes:
            print(f"Process(pid={process.pid}, arrival={process.arrival_time}, burst={process.burst_time}, priority={process.priority})")
        
        # Executar algoritmo Multilevel Queue
        avg_waiting_time, avg_turnaround_time = multilevel_queue(processes)
        
        # Exibir resultados do teste
        print(f"\nResults for Test Run {i+1}:")
        print(f"Average Waiting Time: {avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

