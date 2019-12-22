def add(a,b):
    if not isSmaller(a,b):
        a,b = b,a
    a = a[::-1]
    b = b[::-1]
    result = ""
    carry = 0
    for i in range(len(a)):
        temp = int(a[i]) + int(b[i]) + carry
        if temp >= 10:
            temp -= 10
            carry = 1
        else:
            carry = 0
        result = str(temp) + result
    
    for j in range(i+1,len(b)):
        temp = int(b[j]) + carry
        if temp >= 10:
            temp -= 10
            carry = 1
        else:
            carry = 0
        result = str(temp) + result
    if carry == 1:
        result = str(carry) + result
    return result