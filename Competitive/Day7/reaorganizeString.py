def reorganizeString(S):
        count = {}
        for char in S:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        mA = max(count.keys(),key = count.get)
        mAc = count[mA]
        if 2 * mAc - 1 > len(S):
            return ''
        count.pop(mA)
        res = len(S) * ['']
        res[:2 * mAc:2] = mAc * [mA]
        i = 2 * mAc
        for c in count:
            for _ in range(count[c]):
                if i >= len(S):
                    i = 1
                res[i] = c
                i += 2
        return ''.join(res)