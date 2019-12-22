def perms(lst):
    pos = [0] * len(lst)
    for i in range(len(lst)):
        pos[int(lst[i]) - 1] = i
 
    minn = pos[0] + 1
    maxx = pos[0] + 1
    res = ''
    for j in range(len(pos)):
        temp = pos[j] + 1
        if temp < minn:
            minn = temp
        if temp > maxx:
            maxx = temp
        if (maxx - minn + 1) == (j + 1):
            res += '1'
        else:
            res += '0'
 
    return res
 
 
def main():
    t = int(input())
    while t > 0:
        n = input()
        a = input().split()
        print(perms(a))
        t -= 1
main()