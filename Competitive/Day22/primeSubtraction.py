def solve(x, y):
    temp = x - y
    if temp == 1:
        print("NO")
    else:
        print("YES")

def main():
    t = int(input())
    for i in range(t):
        ipt = input().split()
        solve(int(ipt[0]), int(ipt[1]))

main()