from typing import List

class Process:
    def __init__(self, process_num = 0, arrival_time = 0, burst_time = 0):
        self._process_num = process_num
        self._arrival_time = arrival_time
        self._burst_time = burst_time
        
    def getProcessNum(self):
        return self._process_num
    def getArrivalTime(self):
        return self._arrival_time
    def getBurstTime(self):
        return self._burst_time
    def setBurstTime(self, burst_time):
        self._burst_time = burst_time
    
class ProcessTable:
    def __init__(self):
        self._table = []
        
    def getTable(self):
        table = self._table
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
        
        self._table.append(process)
        
    def updateProcessStatus(self, process_num, status):
        for process in self._table:
            if process["process_num"] == process_num:
                process["status"] = status
                break
            
    def setProcessAttribute(self, process_num = 0, attribute_name = "status", attribute_value = "ready"):
        for process in self._table:
            if process["process_num"] == process_num:
                process[attribute_name] = attribute_value
                break
    
    def _getCellNames(self):
        names: List[str]= []
        for key in self._table[0].keys():
            names.append(key)
            
        return names
    
    def _getTableItems(self):
        items = []
        for process in self._table:
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
            for i in range(len(row)): row[i] = (f"{row[i]} " if i != 0 or is_first_row else f"p{row[i]}") + (column_sizes[i] - len(str(row[i]))) * " "
            row = "| " + " | ".join(row) + " |"
            if is_first_row: self._printRowDivider(row)
            print(row)
            self._printRowDivider(row)
            
    def isAllProcessComplete(self):
        not_terminated = 0
        for process in self._table:
            if process["status"] != "terminated": not_terminated += 1
            
        return not_terminated == 0
    
class Queue:
    def __init__(self):
        self._queue = []
        
    def getQueue(self):
        return self._queue
    
    def setQueue(self, queue):
        self._queue = queue
        
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
        arrival_time_digits = len(str(arrival_time))
        if arrival_time < 10: self._chart.append(f"[p{process_num}]")
        else: self._chart.append((arrival_time_digits // 2 + 1) * " " + f"[p{process_num}]" + (arrival_time_digits // 2 + 1) * " ")
        self._time_stamps.append(arrival_time)
        
    def appendIdle(self, unit_time):
        unit_time_digits = len(str(unit_time))
        if unit_time < 10: self._chart.append("[IDLE]")
        else: self._chart.append((unit_time_digits // 2 + 1) * " " + "[IDLE]" + (unit_time_digits // 2 + 1) * " ")
        self._time_stamps.append(unit_time)
        
    def appendCompletionTime(self, completion_time = 0):
        self._time_stamps.append(completion_time)
        
    def printChart(self):
        chart = "| " + " | ".join(self._chart) + " |"
        print("Gannt Chart:")
        print(4 * " " + chart, end = "\n" + 4 * " ")
        i = 0
        remaining_time_stamp_digits = 0
        for char in chart:
            if i > len(self._time_stamps) - 1: break
            if char == "|":
                print(self._time_stamps[i], end = "")
                remaining_time_stamp_digits = len(str(self._time_stamps[i])) - 1
                i += 1
            elif remaining_time_stamp_digits == 0:
                print(" ", end = "")
            else:
                remaining_time_stamp_digits -= 1
        print()
