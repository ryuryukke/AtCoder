# n = int(input())
# money = 1000
# while True:
#     if money >= n:
#         print(money-n)
#         exit()
#     else:
#         money += 1000
import math
n = int(input())
print(math.ceil(n/1000)*1000 - n)