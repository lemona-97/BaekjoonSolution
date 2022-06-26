while True:
    stack = []
    word = list(input())
    if word[0] == ".":
        break
    else:
        for i in word:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if len(stack) == 0:
                    stack.append(")")
                else:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(")")
            elif i == "[":
                stack.append("[")
            elif i == "]":
                if len(stack) == 0:
                    stack.append("]")
                else:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append("]")
        if len(stack) == 0:
            print("yes")
        else:
            print("no")