n = int(input())
s = input()
stack = []
for string in s:
    if len(stack) < 2:
        stack.append(string)
    else:
        last, sec_last = stack[-1], stack[-2]
        if last == "o" and sec_last == "f":
            if string == "x":
                stack.pop()
                stack.pop()
            else:
                stack.append(string)
        else:
            stack.append(string)
print(len(stack))
