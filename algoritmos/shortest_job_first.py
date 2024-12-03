def shortest_job_first(processes, burst_times):
    n = len(processes)
    sorted_indices = sorted(range(n), key=lambda i: burst_times[i])
    waiting_times = [0] * n
    turnaround_times = [0] * n
    elapsed_time = 0

    for i in sorted_indices:
        waiting_times[i] = elapsed_time
        elapsed_time += burst_times[i]
        turnaround_times[i] = elapsed_time

    return waiting_times, turnaround_times
