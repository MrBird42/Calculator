def add(a: float, b: float) -> float:
    """a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """a and b.b=0 ValueError."""
    if b == 0:
        raise ValueError("Error.")
    return a / b

