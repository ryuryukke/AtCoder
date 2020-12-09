n, q = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(q)]
ages = [0] * n
visited = []
# 一旦気にせずに、年齢決め
for i, (a, b, c) in enumerate(abc):
    a, b, c = a-1, b-1, c
    if i == 0:
        ages[a] = 0
        ages[b] = c
        visited.append(a)
        visited.append(b)
    else:
        if a in visited and b in visited:
            if ages[b] != ages[a] + c:
                print(-1)
                exit()
        elif a in visited and b not in visited:
            ages[b] = ages[a] + c
            visited.append(b)
        elif a not in visited and b in visited:
            ages[a] = ages[b] - c
            visited.append(a)
        else:
            ages[a] = 0
            ages[b] = c
            visited.append(a)
            visited.append(b)
# print(ages)
over_age, down_age = len([age for age in ages if age > 100]), len([age for age in ages if age < 0])

if over_age and down_age:
    print(-1)
elif over_age:
    ages = [age - (max(ages)-100) for age in ages]
    if len([age for age in ages if age < 0]):
        print(-1)
    else:
        print(max(ages)-min(ages))
elif down_age:
    ages = [age + (0-min(ages)) for age in ages]
    if len([age for age in ages if age > 100]):
        print(-1)
    else:
        print(max(ages)-min(ages))
else:
    print(max(ages)-min(ages))

"""
----------------------------------------------------------------------------------------------------
"""

n, q = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(q)]
ages = [0] * n
visited = []
# 一旦気にせずに、年齢決め
for i, (a, b, c) in enumerate(abc):
    a, b, c = a-1, b-1, c
    if i == 0:
        ages[a] = 0
        ages[b] = c
        visited.append(a)
        visited.append(b)
    else:
        if a in visited and b in visited:
            if ages[b] != ages[a] + c:
                print(-1)
                exit()
        elif a in visited and b not in visited:
            ages[b] = ages[a] + c
            visited.append(b)
        elif a not in visited and b in visited:
            ages[a] = ages[b] - c
            visited.append(a)
        else:
            ages[a] = 0
            ages[b] = c
            visited.append(a)
            visited.append(b)

over_age, down_age = len([age for age in ages if age > 100]), len([age for age in ages if age < 0])

if over_age and down_age:
    print(-1)
elif over_age:
    tmp = max(ages) - 100
    ages = [age - tmp for age in ages]
    if len([age for age in ages if age < 0]):
        print(-1)
    else:
        print(max(ages)-min(ages))
elif down_age:
    tmp = 0-min(ages)
    ages = [age + tmp for age in ages]
    if len([age for age in ages if age > 100]):
        print(-1)
    else:
        print(max(ages)-min(ages))
else:
    print(max(ages)-min(ages))

