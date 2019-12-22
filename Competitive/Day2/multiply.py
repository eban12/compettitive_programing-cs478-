import sumWithNegatives

def times(a,b):
    if not add.isSmaller(a,b):
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
        result = add.add(result,temp)
    result = add.trancateZeros(result)
    return result

def main():
    a = input()
    b = input()
    print(int(a) * int(b))
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

if __name__ == '__main__':
    main()





