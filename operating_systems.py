class Process:
    def __init__(self, process_num = 0, arrival_time = 0, burst_time = 0):
        self.__process_num = process_num
        self.__arrival_time = arrival_time
        self.__burst_time = burst_time
        
    def getProcessNum(self):
        return self.__process_num
    def getArrivalTime(self):
        return self.__arrival_time
    def getBurst_time(self):
        return self.__burst_time
    def setBurst_time(self, burst_time):
        self.__burst_time = burst_time
    
class ProcessTable:
    def __init__(self):
        self.__table = []
        
    def getTable(self):
        table = self.__table
        return table
        
    def addProcess(self, process_num = 0, arrival_time = 0, burst_time = 0):
        process = {
            "process_num": process_num,
            "arrival_time": arrival_time,
            "burst_time": burst_time,
            "completion_time": None,
            "response_time": None,
            "turnaround_time": None,
            "waiting_time": None,
            "status": "new"
            }
        
        self.__table.append(process)
        
    def updateProcessStatus(self, process_num, status):
        for process in self.__table:
            if process["process_num"] == process_num:
                process["status"] = "ready"
                break
        
    def printTable(self):
        for process in self.__table:
            for item in process.items(): print(f"p{item[1]}", end="") if item[0] == "process_num" else print(" | ", item[1], end="")
            print()
            
    def isAllProcessComplete(self):
        not_terminated = 0
        for process in self.__table:
            #if process["status"] != "terminated": not_terminated += 1
            if process["status"] != "ready": not_terminated += 1
            
        return  not_terminated == 0
            
class ReadyQueue:
    def __init__(self):
        self.__ready_queue = []
        
    def enqueue(self, process_num, arrival_time, burst_time):
        ready_process = Process(process_num, arrival_time, burst_time)
        self.__ready_queue.append(ready_process)
        
    def dequeue(self):
        self.__ready_queue.pop(0)
        
    def isEmpty(self):
        return len(self.__ready_queue) == 0
        
    def printQueue(self):
        print("Ready: [", end="")
        for ready_process in self.__ready_queue:
            print(f" p{ready_process.getProcessNum()} ", end="")
        print("]")