from collections import defaultdict
n = int(input())
ss = [input() for _ in range(n)]
cache = defaultdict(list)
for s in ss:
    if s[0] == "!":
        if s[1:] not in cache:
            cache[s[1:]].append(2)
        else:
            if cache[s[1:]] != [2]:
                print(s[1:])
                exit()
    else:
        if s not in cache:
            cache[s].append(1)
        else:
            if cache[s] != [1]:
                print(s)
                exit()
print("satisfiable")





