def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
 
def isValid(a, b, x):
    temp = (a * b) / gcd(a, b)
    if temp == x:
        return True
    else:
        return False
 
 
def solve(x):
    if x == 1:
        print(1, 1)
        return
    maxi = x
    ansa = 1
    ansb = x
    limit = int(x ** 0.5) + 1
    for i in range(1, limit):
        if x % i == 0 and isValid(i, x / i, x) and max(i, x/i) < maxi:
            maxi = max(i, x/i)
            ansa = i
            ansb = x // i
    print(ansa, ansb)
 
 
 
def main():
    x = int(input())
    solve(x)
 
main()
