def shuffle(p, q):
    n = len(p)
    while len(q) >= len(p):
        temp = q[:n]
        if sorted(temp) ==sorted(p):
            print("YES")
            return
        q = q[1:]
    print("NO")
 
 
def main():
    t = int(input())
    while t > 0:
        p = input()
        q = input()
        shuffle(p,q)
        t -= 1
main()