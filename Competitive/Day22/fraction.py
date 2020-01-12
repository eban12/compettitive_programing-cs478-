def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
 
def solve(n):
    a = 0
    b = 0
    for i in range(1,n):
        for j in range(i, n):
            if i + j == n and gcd(i, j) == 1 and i > a:
                a = i
                b = j
    print(a, b)
                
 
def main():
    n = int(input())
    solve(n)
 
main()
