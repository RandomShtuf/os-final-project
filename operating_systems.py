from typing import List

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
            
    def setProcessAttribute(self, process_num = 0, attribute_name = "status", attribute_value = "ready"):
        for process in self.__table:
            if process["process_num"] == process_num:
                process[attribute_name] = attribute_value
                break
    
    def _getCellNames(self):
        names: List[str]= []
        for key in self.__table[0].keys():
            names.append(key)
            
        return names
    
    def _getTableItems(self):
        items = []
        for process in self.__table:
            items.append(list(process.values()))
        
        return items
    
    def _getColumnSizes(self, table):
        column_sizes = []
        for i in range(len(table[0])):
            cell_sizes = []
            for row in table: cell_sizes.append(len(str(row[i])))
            column_sizes.append(max(cell_sizes))
        
        return column_sizes
            
    def _printRowDivider(self, row):
        for char in row: print("-", end = "") if char != "|" else print("+", end = "")
        print()
        
    def printTable(self):
        display_table = []
        display_table.append(self._getCellNames())
        display_table += self._getTableItems()
        column_sizes = self._getColumnSizes(display_table)
        
        for row in display_table:
            is_first_row = False 
            if row == display_table[0]: is_first_row = True
            for i in range(len(row)): row[i] = str(row[i]) + (column_sizes[i] - len(str(row[i]))) * " "
            row = "| " + " | ".join(row) + " |"
            if is_first_row: self._printRowDivider(row)
            print(row)
            self._printRowDivider(row)
            
    def isAllProcessComplete(self):
        not_terminated = 0
        for process in self.__table:
            if process["status"] != "terminated": not_terminated += 1
            
        return not_terminated == 0
    
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

class GanttChart:
    def __init__(self):
        self._chart = []
        self._time_stamps = []
        
    def getChart(self):
        return self._chart
        
    def appendProcess(self, process_num = 0, arrival_time = 0):
        self._chart.append(f"p{process_num}")
        self._time_stamps.append(arrival_time)
        
    def appendIdle(self, unit_time):
        self._chart.append("IDLE")
        self._time_stamps.append(unit_time)
        
    def appendCompletionTime(self, completion_time = 0):
        self._time_stamps.append(completion_time)
        
    def printChart(self):
        chart = "|[ " + " ]|[ ".join(self._chart) + " ]|"
        print("Gannt Chart:")
        print(4 * " " + chart, end = "\n" + 4 * " ")
        i = 0
        for char in chart:
            if i > len(self._time_stamps) - 1: break
            print(self._time_stamps[i], end = "") if char == "|" else print(" ", end = "")
            if char == "|": i += 1
        print()