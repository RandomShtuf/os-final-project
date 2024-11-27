class Process:
    def __init__(process_num = 0, arrival_time = 0, burst_time = 0):
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
        
    def addProcess(self, process_num = 0, arrival_time = 0, burst_time = 0):
        process = {
            "process_num": process_num,
            "arrival_time": arrival_time,
            "burst_time": burst_time,
            "completion_time": None,
            "response_time": None,
            "turnaround_time": None,
            "waiting_time": None
            }
        
        self.__table.append(process)
        
    def printTable(self):
        for process in self.__table:
            for item in process.items(): print(f"p{item[1]}", end="") if item[0] == "process_num" else print(" | ", item[1], end="")
            print()