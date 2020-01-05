def fraction(expression):
    expression = expression.replace('-', '+-')
    expression = expression.replace('+', ' ')
    expression = expression.split()
    tokens = [[int(j) for j in i.split('/')] for i in expression]

    result = [0,1]
    for i in tokens:
        result = add(result, i)
    
    return str(result[0]) + '/' + str(result[1])


def add(f1, f2):
    LCM, GCD = lcm(f1[1], f2[1])
    res = []
    res.append((LCM // f1[1]) * f1[0] + (LCM // f2[1]) * f2[0])
    res.append(LCM)

    res[0] = res[0] // GCD
    res[1] = res[1] // GCD
    return res

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    temp = gcd(a, b)
    return (a * b) // temp, temp 

print(fraction("5/3+1/3"))
# print(add([-5,3], [1,3]))

