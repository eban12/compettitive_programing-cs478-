def rearrangeBarcodes(barcodes):
        a = [barcodes[0]]
        b = []
        for i in range(1,len(barcodes)):
            if barcodes[i] == a[len(a) - 1]:
                b.append(barcodes[i])
            else:
                a.append(barcodes[i])
                if len(b) > 0:
                    a.append(b[0])
                    b.pop(0)
        if len(b) == 1:
            if a[-1] != b[0]:
                a.append(b[0])
                b.pop(0)
            elif a[0] != b[0]:
                a = b + a
                b.pop(0)

        for i in range(1,len(a)):
            if len(b) == 0:
                break
            if b[0] != a[i] and b[0] != a[i - 1]:
                a.insert(i,b[0])
                b.pop(0)
        return a