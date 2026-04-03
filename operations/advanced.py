import math

def power(a: float, b: float) -> float:
    """a in b."""
    return a ** b

def sqrt(a: float) -> float:
    """a.a<0 ValueError."""
    if a < 0:
        raise ValueError("koren")
    return math.sqrt(a)

def percent(a: float, b: float) -> float:
    """b ot a.(200, 10) -> 20.0."""
    return a * (b / 100)

