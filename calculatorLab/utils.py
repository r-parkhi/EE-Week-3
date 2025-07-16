# utils.py
import logging;
from datetime import datetime;

def log_call(func):
    def wrapper(*a, **kw):
        ts = datetime.utcnow().isoformat(timespec="seconds");
        result = func(*a, **kw);
        with open("calls.log", "a") as f:
            f.write(f"{ts} {func.__name__}{a}={result}\n");
        return result;
    return wrapper;