def round_robin(processes, quantum):
    time = 0
    queue = processes[:]
    while queue:
        process = queue.pop(0)
        if process.remaining_time > quantum:
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:
            time += process.remaining_time
            process.turnaround_time = time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    return avg_waiting_time, avg_turnaround_time
