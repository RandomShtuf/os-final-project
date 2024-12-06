from os_libs.operating_system import ProcessTable, ReadyQueue, ExecutingQueue, GanttChart
from os_libs.fcfs import schedule as fcfsSchedule
from time import time
from os import system


start_time = time()
process_table = ProcessTable()
ready_queue = ReadyQueue()
executing_queue = ExecutingQueue()
gantt_chart = GanttChart()

#processsCount = int(input("Enter the number of processes: "))
#for i in range(processsCount):
#    arrival_time = int(input(f"Enter arrival time for p{i}: "))
#    burst_time = int(input(f"Enter burst time for p{i}: "))
#    process_table.addProcess(i, arrival_time, burst_time)

# process_table.addProcess(0, 10, 5)
# process_table.addProcess(1, 8, 4)
# process_table.addProcess(2, 12, 4)
# process_table.addProcess(3, 3, 3)
# process_table.addProcess(4, 15, 5)

process_table.addProcess(0, 10, 5)
process_table.addProcess(1, 3, 4)
process_table.addProcess(2, 10, 4)
process_table.addProcess(3, 3, 3)
process_table.addProcess(4, 10, 5)

system("cls")
process_table.printTable()
input("Press Enter To Continue: ")
fcfsSchedule(process_table, ready_queue, executing_queue, gantt_chart)
print(f"time elapsed: ~{time() - start_time: .2f} seconds")