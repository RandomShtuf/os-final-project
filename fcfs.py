from operating_systems import ProcessTable


#processsCount = int(input("Enter the number of processes: "))
process_table = ProcessTable()

#for i in range(processsCount):
#    arrival_time = int(input(f"Enter arrival time for p{i}: "))
#    burst_time = int(input(f"Enter burst time for p{i}: "))
#    process_table.addProcess(i, arrival_time, burst_time)
process_table.addProcess(0, 0, 3)
process_table.addProcess(1, 2, 4)
process_table.addProcess(2, 5, 6)
    
process_table.printTable()