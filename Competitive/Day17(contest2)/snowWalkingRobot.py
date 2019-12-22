def walk(str):
    dic = {"L":0, "R":0, "U":0, "D":0}
    for i in str:
        dic[i] += 1
    
    l = r = min(dic["L"], dic["R"])
    u = d = min(dic["U"], dic["D"])
    
    if u == 0 and l != 0:
        l = r = 1
    elif u != 0 and l == 0:
        u = d = 1
    
    print(l + u + r + d)
    ans = r * "R" + u * "U" + l * "L" + d * "D"
    print(ans)
 
def main():
     q = int(input())
     while q > 0:
         str = input()
         walk(str)
         q -= 1
main()