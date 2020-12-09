# from math import floor
# def kill(life):
#     if life in dp.keys():
#         return dp[life]
#     if life == 1:
#         dp[life] = 1
#         return 1
#     elif life > 1:
#         dp[life] = kill(floor(life/2)) * 2 + 1
#         return dp[life]
# h = int(input())
# dp = {}
# print(kill(h))

def kill(life):
    if life == 1:
        return 1
    elif life > 1:
        return kill(life//2) * 2 + 1
h = int(input())
print(kill(h))
