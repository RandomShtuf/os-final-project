from operating_systems import ProcessTable, ReadyQueue

#processsCount = int(input("Enter the number of processes: "))
process_table = ProcessTable()
ready_queue = ReadyQueue()

def handleArrivingProcess(unit_time):
    for process in process_table.getTable():
        if process["arrival_time"] == unit_time:
            process_table.updateProcessStatus(process["process_num"], "ready")
            ready_queue.enqueue(process["process_num"], process["arrival_time"], process["burst_time"])
    process_table.printTable()
    ready_queue.printQueue()


#for i in range(processsCount):
#    arrival_time = int(input(f"Enter arrival time for p{i}: "))
#    burst_time = int(input(f"Enter burst time for p{i}: "))
#    process_table.addProcess(i, arrival_time, burst_time)
process_table.addProcess(0, 0, 3)
process_table.addProcess(1, 2, 4)
process_table.addProcess(2, 5, 6)
    
process_table.printTable()

unit_time = 0
while not process_table.isAllProcessComplete():
    handleArrivingProcess(unit_time)
        
    unit_time += 1