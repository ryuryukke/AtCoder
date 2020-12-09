N, M = list(map(int, input().split()))
sum = 0
if N >= 2:
    sum += N*(N-1)//2
if M >= 2:
    sum += M*(M-1)//2
print(sum)
