def allCellsDistOrder(R, C, r0, c0):
        cords = []
        for i in range(R):
            for j in range(C):
                dis = abs(i - r0) + abs(j - c0)
                cords.append([dis,[i,j]])
        cords = sorted(cords)
        cords = [k[1] for k in cords]
        return cords