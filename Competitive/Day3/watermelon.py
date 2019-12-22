def check(w):
    if w % 2 == 0 and w != 2:
        return "YES"
    else:
        return "NO"
 
w = input()
print(check(int(w)))