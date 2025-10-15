from enum import Enum, auto

class ProcessState(Enum):
    """
    Enum representing the various states of a process.
    """
    NEW = auto()
    READY = auto()
    RUNNING = auto()
    WAITING = auto()
    TERMINATED = auto()
    
    def __str__(self):
        return self.name

if __name__ == "__main__":
    # Example usage
    state = ProcessState.NEW
    print(f"Current process state: {state}")
    
    state = ProcessState.RUNNING
    print(f"Current process state: {state}")
    
    state = ProcessState.TERMINATED
    print(f"Current process state: {state}")