# Ackermann's Function is a function which can only be wirtten in recursive and not converted to Loops

def ack(m, n):
    if m == 0: return n + 1
    elif n == 0: return ack(m - 1, 1)
    else: return ack(m - 1, ack(m, n - 1))
