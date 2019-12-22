def minimumPairWise(a, b, c):
    lst = []
    state = [1, 0, -1]
    for i in range(3):
        x = a + state[i]
        for k in range(3):
            y = b + state[k]
            for j in range(3):
                z = c + state[j]
                lst.append(totalPaireWise(x, y, z))
    print(min(lst))
 
 
def totalPaireWise(a, b, c):
    return abs(a - b) + abs(a - c) + abs(b - c)
 
def main():
    q = int(input())
    while q > 0:
        inpt = input().split()
        minimumPairWise(int(inpt[0]), int(inpt[1]), int(inpt[2]))
        q -= 1
 
main()