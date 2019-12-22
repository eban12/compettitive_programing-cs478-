def isSmaller(a,b):
    '''checks weather a is less than b or not'''

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
    '''removes leading zeros from the output result'''

    while result[0] == '0' and len(result) > 1:
        result = result[1:]
    return result

def add(a,b):
    '''sums non-negative numbers a and b'''

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
    '''subtracts non-negative numbers a and b'''

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

def times(a,b):
    '''multiplies non-negative numbers a and b'''

    if not isSmaller(a,b):
        a,b = b,a
    
    a = a[::-1]
    b = b[::-1]
    result = "0"
    for i in range(len(a)):
        temp = ""
        carry = 0
        for j in range(len(b)):
            t = int(a[i]) * int(b[j]) + carry
            if t >= 10:
                s = t
                t = s % 10
                carry = s // 10
            else:
                carry = 0
            temp = str(t) + temp
        if carry != 0:
            temp = str(carry) + temp
        temp = temp + ('0' * i)
        result = add(result,temp)
    result = trancateZeros(result)
    return result

def multiples(a,b):
    '''returns 1-9 multiples of b that are less than a'''

    lst = [b]
    i = 2
    temp = times(b,str(i))
    while (isSmaller(temp,a) or temp == a) and i < 10:
        lst.append(temp)
        i += 1
        temp = times(b,str(i))
    return lst

def divide(a,b):
    '''devides non-negative numbers a and b (integer division only)'''

    multiple = multiples(a,b)
    result = "0"
    i = len(multiple) - 1
    while isSmaller(b,a) or a == b:
        temp = multiple[i]
        n = len(temp) - 1
        while isSmaller(temp,a) or temp == a:
            a = subtract(a,temp)
            result =  add(result,str(i + 1))
        i -= 1
    return  result

def addition(a,b):
    '''determination of the two values sign and presentation of 
    result in correct form for addition'''

    #print(int(a) + int(b))
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

def subtraction(a,b):
    '''determination of the two values sign and presentation of 
    result in correct form for subtraction'''

    #print(int(a) - int(b))
    if b[0] != '-':
        addition(a,'-' + b)
    else:
        addition(a,b[1:])

def multiplication(a,b):
    '''determination of the two values sign and presentation of 
    result in correct form for multiplication'''

    #print(int(a) * int(b))
    if a == '0' or b == '0':
        print('0')
    elif (a[0] == '-' and b[0] == '-'):
        print(times(a[1:],b[1:]))
    elif a[0] == '-':
        print('-' + times(a[1:],b))
    elif b[0] == '-':
        print('-' + times(a,b[1:]))
    else:
        print(times(a,b))

def division(a,b):
    '''determination of the two values sign and presentation of 
    result in correct form for division'''

    #print(int(a) / int(b))
    if a == '0' and b != '0':
        print('0')
    elif b == '0':
        print("Error! Invalid operation, division By Zero!")
    elif a[0] == '-' and b[0] == '-':
        print(divide(a[1:],b[1:]))
    elif a[0] == '-':
        print('-' + divide(a[1:],b))
    elif b[0] == '-':
        print('-' + divide(a,b[1:]))
    else:
        print(divide(a,b))

def main():
    '''oprator determination'''

    inpt = input().split()
    if inpt[1] == '+':
        addition(inpt[0],inpt[2])
    elif inpt[1] == '-':
        subtraction(inpt[0],inpt[2])
    elif inpt[1] == '*':
        multiplication(inpt[0],inpt[2])
    elif inpt[1] == '/':
        division(inpt[0],inpt[2])
    else:
        print('Invalid Operator!')

if __name__ == "__main__":
    main()

