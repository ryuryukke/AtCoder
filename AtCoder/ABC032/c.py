# n, k = map(int, input().split())
# s = [int(input()) for _ in range(n)]
# i, j, tmp, ans = 0, 0, 1, 0
# if 0 in s:
#     print(n)
# else:
#     for i in range(n):
#         while j < n and tmp*s[j] <= k:
#             tmp *= s[j]
#             j += 1
#         ans = max(ans, j-i)
#         if i == j:
#             j += 1
#         else:
#             tmp //= s[i]
#     print(ans)


# 8queen問題とくわ



def left_up(place, mass):
    flag = False
    for i, v in enumerate(place):
        while i > 0 and v > 0:
            i -= 1
            v -= 1
            if mass[i][v] == "Q":
                flag = True
    return flag
def left_down(place, mass):
    flag = False
    for i, v in enumerate(place):
        while i < 7 and v > 0:
            i += 1
            v -= 1
            if mass[i][v] == "Q":
                flag = True
    return flag

def right_up(place, mass):
    flag = False
    for i, v in enumerate(place):
        while i > 0 and v < 7:
            i -= 1
            v += 1
            if mass[i][v] == "Q":
                flag = True
    return flag

def right_down(place, mass):
    flag = False
    for i, v in enumerate(place):
        while i < 7 and v < 7:
            i += 1
            v += 1
            if mass[i][v] == "Q":
                flag = True
    return flag

def helper(place):
    flag = False
    mass = [["."] * 8 for _ in range(8)]
    for i, v in enumerate(place):
        mass[i][v] = "Q"
    if left_up(place, mass) and left_down(place, mass) and right_up(place, mass) and right_down(place, mass):
        return mass
    return None

import itertools
k = int(input())
rc = [tuple(map(int, input().split())) for _ in range(k)]
for select in itertools.permutations(list(range(8))):
    for r, c in rc:
        if select[r] != c:
            break
    else:
        res = helper(select)
        if not res:
            continue
        else:
            print(res)
            exit()
