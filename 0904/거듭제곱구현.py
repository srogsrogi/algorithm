def calculate(a, n):
    if n == 0:
        return 1
    else:
        return a * calculate(a, n-1)

print(calculate(2,4))