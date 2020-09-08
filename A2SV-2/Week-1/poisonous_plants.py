# Simulation (slow version)
def poisonousPlants(p):
    ans = -1
    nextDay = True
    while nextDay:
        nextDay = False
        temp = [p[0]]
        for i in range(1,len(p)):
            if p[i] <= p[i-1]:
                temp.append(p[i])
            else:
                nextDay = True
        p = temp
        ans += 1
    return ans

# Optimal solution
def poisonousPlants(p):
    ans = -float('inf')
    stack = []
    for plant in p:
        days = 1
        while stack and stack[-1][0] >= plant:
            temp = stack.pop()[1]
            days = max(days, temp + 1)
        
        if not stack:
            days = 0
        stack.append((plant, days))
        ans = max(ans, days)
        
    return ans
