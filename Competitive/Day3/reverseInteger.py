def reverse(x):
        if x < (-2 ** 31) or x > (2 ** 31):
            return 0
        
        x = str(x)
        signed = False
        if x[0] == '-':
            signed = True
            x = x[1:]
            x = x[::-1]
        else:
            x = x[::-1]
        
        while x[0] == '0' and  len(x) > 1:
            x = x[1:]
        
        if signed:
            return int('-' + x)
        return int(x)