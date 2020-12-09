N = int(input())
X = list(map(int, input().split()))
ave = round(sum(X)/N)
s = [(i-ave)**2 for i in X]
print(sum(s))
