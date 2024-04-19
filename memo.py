factorial_memo = {}
fibdict = {0: 0, 1: 1}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

def fibMem2(n, fibdict):
    if n in fibdict:
        return fibdict[n]
    else:
        fibdict[n] = fibMem2(n - 1, fibdict) + fibMem2(n - 2,fibdict)
        return fibdict[n]

mem2= fibMem2(14, fibdict)
print(mem2)
result = factorial(14)
print(result)