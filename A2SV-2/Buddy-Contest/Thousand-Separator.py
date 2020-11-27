class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        result = []
        temp = []
        n = list(reversed(str(n)))
        for i in range(len(n)):
            temp.append(n[i])
            if (i+1) % 3 == 0:
                temp.reverse()
                result.append(''.join(temp))
                temp = []
        if temp:
            temp.reverse()
            result.append(''.join(temp))
        result.reverse()
        return '.'.join(result)
