class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        minus = ''
        if (numerator < 0 and denominator > 0) or (denominator < 0 and numerator > 0):
            minus = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        res = [str(numerator // denominator) + "."]
        sub = [numerator % denominator]
        numerator %= denominator
        while numerator != 0:
            numerator *= 10
            res_digit, numerator = divmod(numerator, denominator)
            res.append(str(res_digit))

            if numerator not in sub:
                sub.append(numerator)
            else:
                res.insert(sub.index(numerator) + 1, '(')
                res.append(')')
                break
        temp = "".join(res)
        if temp[-1] == '.':
            return minus + temp[:-1]
        return minus + temp
