def isSmaller(a,b):
    if len(a) < len(b):
        return True
    elif len(b) < len(a):
        return False
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                return True
            elif b[i] < a[i]:
                return False

def trancateZeros(result):
    while result[0] == '0' and len(result) > 1:
        result = result[1:]
    return result

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

def subtract(a,b):
    if isSmaller(a,b):
        a,b = b,a
    
    a = a[::-1]
    b = b[::-1]
    result = ""
    carry = 0
    for i in range(len(b)):
        temp = int(a[i]) - int(b[i]) - carry
        if temp < 0:
            temp += 10 
            carry = 1
        else:
            carry = 0
        result = str(temp) + result
    
    for j in range(i + 1,len(a)):
        temp = int(a[j]) - carry
        if temp < 0:
            temp += 10 
            carry = 1
        else:
            carry = 0
        result = str(temp) + result
    
    result = trancateZeros(result)   
    return result

def main():
    a = input()
    b = input()
    print(int(a) + int(b))
    if a[0] == '-' and b[0] == '-':
        print('-' + add(a[1:],b[1:]))
    elif a[0] == '-':
        temp = subtract(a[1:],b)
        if isSmaller(a,b) or temp == '0':
            print(temp)
        else:
            print('-' + temp)
    elif b[0] == '-':
        temp = subtract(a,b[1:])
        if isSmaller(b[1:],a) or temp == '0':
            print(temp)
        else:
            print('-' + temp)
    else:
        print(add(a,b))

if __name__ == '__main__':       
    main()