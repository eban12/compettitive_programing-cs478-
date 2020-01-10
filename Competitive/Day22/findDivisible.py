def find(a, b):
    if b % a == 0:
        print(a, b)
        return
    limit = b // a
    for i in range(2,limit + 1):
        if i * a <= b:
            print(a, i * a)
            return


def main():
    t = int(input())
    while t > 0:
        ipt = input().split()
        find(int(ipt[0]), int(ipt[1]))
        t -= 1
main()