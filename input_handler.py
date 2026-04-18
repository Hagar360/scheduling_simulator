class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

    def __repr__(self):
        return f"Process(pid={self.pid}, AT={self.arrival_time}, BT={self.burst_time})"
        from process import Process
import random
import csv

def input_manually():
    processes = []
    n = int(input("عدد العمليات: "))
    for i in range(n):
        pid = i + 1
        at = int(input(f"Arrival Time للعملية {pid}: "))
        bt = int(input(f"Burst Time للعملية {pid}: "))
        processes.append(Process(pid, at, bt))
    return processes

def generate_random(n=5):
    processes = []
    for i in range(n):
        at = random.randint(0, 10)
        bt = random.randint(1, 10)
        processes.append(Process(i+1, at, bt))
    return processes

def read_from_file(filename="sample_data.csv"):
    processes = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Process(int(row['pid']),
                       int(row['arrival_time']),
                       int(row['burst_time']))
            processes.append(p)
    return processes

def display_processes(processes):
    print(f"\n{'PID':<6} {'Arrival':<10} {'Burst':<8} {'Priority':<8}")
    print("-" * 35)
    for p in processes:
        print(f"{p.pid:<6} {p.arrival_time:<10} {p.burst_time:<8} {p.priority:<8}")