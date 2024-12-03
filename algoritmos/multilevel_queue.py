def multilevel_queue(processes, burst_times, priorities):
    n = len(processes)
    priority_levels = sorted(set(priorities))
    queues = {level: [] for level in priority_levels}

    for i in range(n):
        queues[priorities[i]].append((processes[i], burst_times[i]))

    waiting_time_dict = {p: 0 for p in processes}
    turnaround_time_dict = {p: 0 for p in processes}
    current_time = 0

    for level in priority_levels:
        queue_processes = queues[level]
        for process, bt in queue_processes:
            waiting_time_dict[process] = current_time
            current_time += bt
            turnaround_time_dict[process] = waiting_time_dict[process] + bt

    waiting_times = [waiting_time_dict[p] for p in processes]
    turnaround_times = [turnaround_time_dict[p] for p in processes]

    return waiting_times, turnaround_times
