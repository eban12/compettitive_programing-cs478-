def canBeGarland(colors):
    bigger = max(colors)
    colors.remove(bigger)
    if bigger - sum(colors) >= 2:
        return False
    else:
        return True

def main():
    t = int(input())
    for i in range(t):
        colors = [int(j) for j in input().split()]
        if canBeGarland(colors):
            print("YES")
        else:
            print("NO")
main()
