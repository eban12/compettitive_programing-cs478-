def beautiful(s):
    for i in range(1,len(s)):
        if s[i] == s[i - 1] and s[i] != '?':
            print(-1)
            return
    s = list(s)
 
    for i in range(1,len(s)):
        v = ['?','a', 'b', 'c']
        if s[i] == '?':
            v.remove(s[i - 1])
            if i < len(s) - 1 and s[i + 1] in v:
                v.remove(s[i + 1])
            s[i] = v.pop()
 
    if s[0] == '?':
        v = ['?','a','b','c']
        if len(s) > 1:
            v.remove(s[1])
        s[0] = v.pop()
 
    for i in s:
        print(i,end='')
    print()
 
 
def main():
    t = int(input())
    while t > 0:
        a = input()
        beautiful(a)
        t -= 1
main()