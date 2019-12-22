import random

def randomize(lst):
    for i in range(len(lst)):
        randIndex = random.randint(i,len(lst)-1)
        lst[i],lst[randIndex] = lst[randIndex],lst[i]
    return lst

lst = [1,2,3,4,5,7,8,9,10]
print(randomize(lst))