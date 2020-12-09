n = int(input())
a = list(map(int, input().split()))
money = 1000
bnf = 0
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        bnf = (money // a[i]) * (a[i+1]-a[i])
        money += bnf
print(money)