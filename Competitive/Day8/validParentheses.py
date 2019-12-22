def isValid(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    brackets = {'(' : ')', '[': ']', '{' : '}'}
    for i in s:
        if i in brackets.keys():
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if brackets[temp] != i:
                return False
    if len(stack) != 0:
        return False
    return True