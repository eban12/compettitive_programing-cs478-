def substring(str, lst):
    lst = [i for i in lst]
    temp = 0
    ans = 0
    for i in str:
        if i in lst:
            temp += 1
        else:
            ans += plustorial(temp)
            temp = 0
    if temp != 0:
        ans += plustorial(temp)
 
    print(ans)
 
 
def plustorial(n):
    return (n * (n + 1)) // 2
 
 
def main():
    n = input()
    str = input()
    lst = input()
    substring(str, lst)
main()