class NegativeNumberError(ValueError):
    """Exception raised for errors in the input if the number is negative."""

    def __init__(self, value):
        self._value = value
    
    def getValue(self):
        return self._value
    
    def __str__(self):
        return f"NegativeNumberError: {self.getValue()} is negative."
    
def checkIfNegative(value):
    if value < 0:
        raise NegativeNumberError(value)
    return value

def checkMemoryLimits():
    lower_limit = checkIfNegative(int(input("Enter lower memory limit: ")))
    upper_limit = checkIfNegative(int(input("Enter upper memory limit: ")))
    if upper_limit <= lower_limit:
        raise ValueError("Upper memory limit must be greater than lower memory limit.")
    return (lower_limit, upper_limit)
