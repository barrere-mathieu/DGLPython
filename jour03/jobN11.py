def fact(n: int = 0):
    if n < 0:
        return 'ERROR -> Enter positive integer'
    elif n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(8))
print(fact(0))
print(fact(-1))