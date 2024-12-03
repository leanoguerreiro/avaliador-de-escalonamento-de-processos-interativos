def round_robin(processes, burst_times, quantum):
    n = len(processes)
    remaining_times = list(burst_times)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_times[i] > 0:
                done = False
                if remaining_times[i] > quantum:
                    time += quantum
                    remaining_times[i] -= quantum
                else:
                    time += remaining_times[i]
                    waiting_times[i] = time - burst_times[i]
                    remaining_times[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

    return waiting_times, turnaround_times
