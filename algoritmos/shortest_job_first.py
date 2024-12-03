def shortest_job_first(processes):
    time = 0
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Ordena por tempo de chegada e burst
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time  # Espera até o processo chegar
        time += process.burst_time
        process.turnaround_time = time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    return avg_waiting_time, avg_turnaround_time
