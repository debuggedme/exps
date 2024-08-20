def evalRPN(tokens=["2","1","+","3","*"]):
        opt = {'+': 0, '-': 0, '*': 1, '/': 1}
        nus = []

        i = 0
        while i < len(tokens):
            if not tokens[i] in opt: nus.append(int(tokens[i]))
            if tokens[i] in opt:
                n2 = nus.pop()
                n1 = nus.pop()
                nus.append(int(eval(str(n1) + tokens[i] + str(n2))))

            i += 1
        return nus[-1]
evalRPN()