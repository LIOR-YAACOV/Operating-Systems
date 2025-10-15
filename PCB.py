from process_state import ProcessState
from input_validation import checkIfNegative, NegativeNumberError, checkMemoryLimits

class PCB:
    def __init__(self):
        self._state = ProcessState(checkIfNegative(int(input("Enter process state: "))))
        self._process_id = checkIfNegative(int(input("Enter process ID: ")))
        self._program_counter = checkIfNegative(int(input("Enter process program counter: ")))
        self._registers = []
        num_registers = checkIfNegative(int(input("Enter number of registers: ")))
        for i in range(num_registers):
            reg_value = checkIfNegative(int(input(f"Enter value for register {i}: ")))
            self._registers.append(reg_value)
        self._memory_limits = checkMemoryLimits()
        self._list_of_open_files = []
        num_files = checkIfNegative(int(input("Enter number of open files: ")))
        for i in range(num_files):
            file_name = input(f"Enter name for open file {i}: ")
            self._list_of_open_files.append(file_name)
            
    def getState(self):
        return self._state
    
    def getProcessID(self):
        return self._process_id
    
    def getProgramCounter(self):
        return self._program_counter
    
    def getRegisters(self):
        return self._registers
    
    def getMemoryLimits(self):
        return self._memory_limits
    
    def getListOfOpenFiles(self):
        return self._list_of_open_files
    
    def printProcess(self):
        print(f"Process ID: {self.getProcessID()}")
        print(f"State: {self.getState()}")
        print(f"Program Counter: {self.getProgramCounter()}")
        for i in range(len(self.getRegisters())):
            print(f"Register {i}: {self.getRegisters()[i]}")
        print(f"Memory Limits: {self.getMemoryLimits()}")
        for i in range(len(self.getListOfOpenFiles())):
            print(f"Open File {i}: {self.getListOfOpenFiles()[i]}")
    
    
if __name__ == "__main__":
    try:
        pcb = PCB()
        pcb.printProcess()
    except NegativeNumberError as e:
        print(e)
    except ValueError as ve:
        print(f"ValueError: {ve}")