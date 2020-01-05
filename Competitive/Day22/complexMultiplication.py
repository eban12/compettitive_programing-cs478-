def complexMult(a, b):
    aTokens = getTokens(a)
    bTokens = getTokens(b)
    real = (aTokens[0] * bTokens[0]) - (aTokens[1] * bTokens[1])
    imaginary = ((aTokens[0] * bTokens[1]) + (aTokens[1] * bTokens[0]))
    return str(real) + '+' + str(imaginary) + 'i' 

def getTokens(complex):
    tokens = complex.split('+')
    tokens[1] = tokens[1][:-1]
    tokens = [int(i) for i in tokens]
    return tokens

# a = '1+-1i'
# b = '1+0i'
# print(complexMult(a,b))