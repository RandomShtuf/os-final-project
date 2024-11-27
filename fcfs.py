from operating_systems import ProcessTable, ReadyQueue, ExecutingQueue
from time import sleep
from os import system

#processsCount = int(input("Enter the number of processes: "))
process_table = ProcessTable()
ready_queue = ReadyQueue()
executing_queue = ExecutingQueue()

def handleArrivingProcess(unit_time):
    for process in process_table.getTable():
        if process["arrival_time"] == unit_time:
            process_table.updateProcessStatus(process["process_num"], "ready")
            ready_queue.enqueue(process["process_num"], process["arrival_time"], process["burst_time"])
    
def executeReadyProcess():
    temp = ready_queue.dequeue()
    executing_queue.enqueue(temp)
    process_table.updateProcessStatus(temp.getProcessNum(), "executing")
        
def handleExecutingProcess():
    burst_time = executing_queue.peek().getBurstTime()
    if burst_time == 0:
        temp = executing_queue.dequeue()
        process_table.updateProcessStatus(temp.getProcessNum(), "terminated")
        return
    executing_queue.peek().setBurstTime(burst_time - 1)


#for i in range(processsCount):
#    arrival_time = int(input(f"Enter arrival time for p{i}: "))
#    burst_time = int(input(f"Enter burst time for p{i}: "))
#    process_table.addProcess(i, arrival_time, burst_time)
process_table.addProcess(0, 0, 3)
process_table.addProcess(1, 2, 4)
process_table.addProcess(2, 5, 6)
    
process_table.printTable()
input("Press Enter To Continue: ")

unit_time = 0
while not process_table.isAllProcessComplete():
    system("cls")
    print(f"Unit Time: {unit_time}")
    if not executing_queue.isEmpty():
        handleExecutingProcess()
    handleArrivingProcess(unit_time)
    if executing_queue.isEmpty() and not ready_queue.isEmpty():
        executeReadyProcess()
    process_table.printTable()
    executing_queue.printQueue("Executing")
    ready_queue.printQueue("Ready")
        
    unit_time += 1
    sleep(2)