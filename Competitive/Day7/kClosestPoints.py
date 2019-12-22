def kClosest(points, K):
        dis = []
        for i in points:
            d = i[0] ** 2 + i[1] ** 2
            dis.append([d,i])
   
        dis = sorted(dis)
        res = []
        for i in range(K):
            res.append(dis[i][1])
        return res