def how_many(n,m,a):
    temp1 = n // a
    if n % a != 0:
        temp1 += 1
    
    temp2 = m // a
    if m % a != 0:
        temp2 += 1
    
    return temp1 * temp2
    
inp = [int(i) for i in input().split()]
print(how_many(inp[0],inp[1],inp[2]))