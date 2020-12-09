T = list(input())
for i in range(len(T)):
    if i == 0:
        if T[i] == "?":
            if len(T) == 1:
                T[i] = "D"
                break
            if T[i+1] == "D":
                T[i] = "P"
            else:
                T[i] = "D"
    else:
        if T[i] == "?":
            T[i] = "D"
print("".join(T))

