from Process import Process
def multilevel_queue(processes):
    high_priority_queue = [p for p in processes if p.priority == 'high']
    low_priority_queue = [p for p in processes if p.priority == 'low']

    print("\n=== High Priority Queue ===")
    for process in high_priority_queue:
        print(f"Process(pid={process.pid}, arrival={process.arrival_time}, burst={process.burst_time})")

    print("\n=== Low Priority Queue ===")
    for process in low_priority_queue:
        print(f"Process(pid={process.pid}, arrival={process.arrival_time}, burst={process.burst_time})")

    def execute_queue(queue, quantum=None):
        time = 0
        while queue:
            process = queue.pop(0)
            if time < process.arrival_time:
                time = process.arrival_time
            
            print(f"\nExecuting Process: {process.pid} | Remaining Time: {process.remaining_time} | Current Time: {time}")
            
            if quantum and process.remaining_time > quantum:
                time += quantum
                process.remaining_time -= quantum
                queue.append(process)
            else:
                time += process.remaining_time
                process.turnaround_time = time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                print(f"Process {process.pid} completed | Waiting Time: {process.waiting_time} | Turnaround Time: {process.turnaround_time}")

    execute_queue(high_priority_queue, quantum=3)
    execute_queue(low_priority_queue)

    all_processes = high_priority_queue + low_priority_queue
    
    if len(all_processes) == 0:
        return 0, 0

    avg_waiting_time = sum(p.waiting_time for p in all_processes) / len(all_processes)
    avg_turnaround_time = sum(p.turnaround_time for p in all_processes) / len(all_processes)

    print(f"\n=== Results ===\nAverage Waiting Time: {avg_waiting_time:.2f}\nAverage Turnaround Time: {avg_turnaround_time:.2f}\n")

    return avg_waiting_time, avg_turnaround_time

# Exemplo de uso com mensagens de depuração
if __name__ == "__main__":
    processes = [
        Process(0, 5, 9, 'low'),
        Process(1, 10, 5, 'low'),
        Process(2, 3, 8, 'high'),
        Process(3, 6, 8, 'low'),
        Process(4, 9, 9, 'high'),
        Process(5, 8, 3, 'high'),
        Process(6, 0, 8, 'low'),
        Process(7, 10, 10, 'high'),
        Process(8, 3, 5, 'high'),
        Process(9, 8, 1, 'low')
    ]
    
    avg_waiting_time, avg_turnaround_time = multilevel_queue(processes)
