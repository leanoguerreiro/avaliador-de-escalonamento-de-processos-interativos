class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, priority={self.priority})")
