def operation(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

op = operation(2, 5)
print(op)
print(type(op))

o, p, e = operation(2, 5)   # Unpacking the tuple
print(o, p, e)
print(type(o))
print(type(p))
print(type(e))