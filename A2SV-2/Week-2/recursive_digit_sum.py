def superDigit(n, k):
    s = 0
    for i in n:
        s += int(i) * k
    return solve(str(s))
    
def solve(n):
    if len(n) == 1:
        return n
    s = 0
    for i in n:
        s += int(i)
    return solve(str(s))
