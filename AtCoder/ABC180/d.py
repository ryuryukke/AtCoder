from math import log2
# from math import 
"""
今回の問題はwhileとかifの条件式の書き方が悪かったため、汚い書き方になった
&&
a倍していくところは計算量えぐいと思ったため、log計算とか持ち出してしまったが、
計算量はO(logY)のため、大丈夫であることに気づいていなかった

"""

x, y, a, b = map(int, input().split())
ans = 0
while 1:
    if x >= y:
        print(ans - 1)
        exit()
    if (a-1) * x > b:
        break
    ans += 1
    x *= a
ans += (y-x-1) // b
print(ans)



