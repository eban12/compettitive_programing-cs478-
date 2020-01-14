def solve(s):
    numL = s.count('L')
    numR = s.count('R')
    print(numL + numR + 1)
 
 
def main():
    n = input()
    s = input()
    solve(s)
 
main()
