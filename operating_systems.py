class Process:
    def __init__(self, process_num = 0, arrival_time = 0, burst_time = 0):
        self.__process_num = process_num
        self.__arrival_time = arrival_time
        self.__burst_time = burst_time
        
    def getProcessNum(self):
        return self.__process_num
    def getArrivalTime(self):
        return self.__arrival_time
    def getBurstTime(self):
        return self.__burst_time
    def setBurstTime(self, burst_time):
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
                process["status"] = status
                break
        
    def printTable(self):
        for process in self.__table:
            for item in process.items(): print(f"p{item[1]}", end="") if item[0] == "process_num" else print(" | ", item[1], end="")
            print()
            
    def isAllProcessComplete(self):
        not_terminated = 0
        for process in self.__table:
            if process["status"] != "terminated": not_terminated += 1
            
        return  not_terminated == 0
    
class Queue:
    def __init__(self):
        self._queue = []
        
    def peek(self):
        return self._queue[0]
        
    def enqueue(self, process):
        self._queue.append(process)
        
    def dequeue(self):
        return self._queue.pop(0)
        
    def isEmpty(self):
        return len(self._queue) == 0
    
    def printQueue(self, queue_name = "Queue"):
        print(f"{queue_name}: [", end="")
        for process in self._queue:
            print(f" p{process.getProcessNum()} ", end="")
        print("]")
            
class ReadyQueue(Queue):
    def enqueue(self, process_num, arrival_time, burst_time):
        process = Process(process_num, arrival_time, burst_time)
        self._queue.append(process)
        
class ExecutingQueue(Queue):
    pass