def maxSub(lst):
    local_max = 0
    global_max = -2**32
    for i in range(len(lst)):
        local_max = max(lst[i], lst[i] + local_max)
        if local_max > global_max:
            global_max = local_max 
 
    return global_max
 
def solve(lst):
    yasr = sum(lst)
    adel = max(maxSub(lst[1:]), maxSub(lst[:-1]))
    if yasr > adel:
        print("YES")
    else:
        print("NO")
 
def main():
    t = int(input())
    for i in range(t):
        n = input()
        lst = [int(j) for j in input().split()]
        solve(lst)
 
main()
