from os_libs.operating_system import ProcessTable, ReadyQueue, ExecutingQueue, GanttChart
#from operating_system import ProcessTable, ReadyQueue, ExecutingQueue, GanttChart
from os_libs.queue_sorter import sortByAttribute
#from queue_sorter import sortByAttribute
from time import sleep
from os import system


def handleArrivingProcess(process_table, ready_queue, unit_time, remaining_new_processes):
    for process in process_table.getTable():
        if process["arrival_time"] == unit_time:
            process_table.setProcessAttribute(process["process_num"], "status", "ready")
            ready_queue.enqueue(process["process_num"], process["arrival_time"], process["burst_time"])
            remaining_new_processes -= 1
            
    ready_queue.setQueue(sortByAttribute(ready_queue, "process_num"))
    ready_queue.setQueue(sortByAttribute(ready_queue, "arrival_time"))
            
    return remaining_new_processes
            
    
def executeReadyProcess(process_table, ready_queue, executing_queue, gantt_chart, unit_time):
    temp = ready_queue.dequeue()
    executing_queue.enqueue(temp)
    process_table.setProcessAttribute(temp.getProcessNum(), "status", "executing")
    process_table.setProcessAttribute(temp.getProcessNum(), "response_time", unit_time - temp.getArrivalTime())    
    gantt_chart.appendProcess(temp.getProcessNum(), unit_time)
        
def handleExecutingProcess(process_table, executing_queue, unit_time):
    executing_queue.peek().setBurstTime(executing_queue.peek().getBurstTime() - 1)
    burst_time = executing_queue.peek().getBurstTime()
    process_num = executing_queue.peek().getProcessNum()
    if burst_time == 0:
        temp = executing_queue.dequeue()
        process_table.setProcessAttribute(temp.getProcessNum(), "status", "terminated")
        process_table.setProcessAttribute(process_num, "completion_time", unit_time)
        return

def handleIdle(gantt_chart, unit_time):
    if not "IDLE" in gantt_chart.getChart()[-1]:
        gantt_chart.appendIdle(unit_time)
        
def isSchedulingComplete(process_table, gantt_chart, unit_time):
    if process_table.isAllProcessComplete():
        gantt_chart.appendCompletionTime(unit_time)
        return True
    else:
        return False
        
def schedule(process_table, ready_queue, executing_queue, gantt_chart):
    unit_time = 0
    is_idle = True
    remaining_new_processes = len(process_table.getTable())
    
    while True:
        system("cls")
        print(f"Unit Time: {unit_time}")
        if not executing_queue.isEmpty():
            is_idle = False
            handleExecutingProcess(process_table, executing_queue, unit_time)
            if isSchedulingComplete(process_table, gantt_chart, unit_time): break
        if remaining_new_processes != 0:
            remaining_new_processes = handleArrivingProcess(process_table, ready_queue, unit_time, remaining_new_processes)
        if executing_queue.isEmpty() and not ready_queue.isEmpty():
            executeReadyProcess(process_table, ready_queue, executing_queue, gantt_chart, unit_time)
            is_idle = False
        elif executing_queue.isEmpty():
            is_idle = True
        if is_idle and unit_time == 0:
            gantt_chart.appendIdle(unit_time)
        elif is_idle:
            handleIdle(gantt_chart, unit_time)
        process_table.printTable()
        gantt_chart.printChart()
        executing_queue.printQueue("Executing")
        ready_queue.printQueue("Ready")
        #print(f"remaining new processes: {remaining_new_processes}")
        #input("Press Enter To Continue: ")
            
        unit_time += 1
        sleep(1)
        
    bt_sum = 0
    tt_sum = 0
    wt_sum = 0
    for process in process_table.getTable():
        process_table.setProcessAttribute(process["process_num"], "turnaround_time", process["completion_time"] - process["arrival_time"])
        process_table.setProcessAttribute(process["process_num"], "waiting_time", process["turnaround_time"] - process["burst_time"])
        bt_sum += process["burst_time"]
        tt_sum += process["turnaround_time"]
        wt_sum += process["waiting_time"]
        
    process_table.printTable()
    gantt_chart.printChart()
    print(f"Turnaround Time Average: {tt_sum / len(process_table.getTable()): .2f}")
    print(f"Waiting Time Average: {wt_sum / len(process_table.getTable()): .2f}")
    print(f"CPU Utilization: {(bt_sum / unit_time) * 100: .2f}%")


if __name__ == "__main__":
    process_table = ProcessTable()
    ready_queue = ReadyQueue()
    executing_queue = ExecutingQueue()
    gantt_chart = GanttChart()
    
    #processsCount = int(input("Enter the number of processes: "))
    #for i in range(processsCount):
    #    arrival_time = int(input(f"Enter arrival time for p{i}: "))
    #    burst_time = int(input(f"Enter burst time for p{i}: "))
    #    process_table.addProcess(i, arrival_time, burst_time)
    process_table.addProcess(2, 0, 3)
    process_table.addProcess(1, 0, 4)
    process_table.addProcess(0, 5, 6)

#     process_table.addProcess(0, 10, 5)
#     process_table.addProcess(1, 8, 4)
#     process_table.addProcess(2, 12, 4)
#     process_table.addProcess(3, 3, 3)
#     process_table.addProcess(4, 15, 5)

    system("cls")
    process_table.printTable()
    input("Press Enter To Continue: ")
    schedule(process_table, ready_queue, executing_queue, gantt_chart)