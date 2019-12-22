def evalRPN(tokens: List[str]) -> int:
        stack = []
        operators = '*/+-'
        for i in tokens:
            if i in operators:
                a = stack.pop()
                b = stack.pop()
                t = int(eval(b + ' ' + i + ' ' + a))
                stack.append(str(t))
            else:
                stack.append(i)
        return stack.pop()