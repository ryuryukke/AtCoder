h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
Min = float("inf") 
Sum = 0
for i in a:
    Sum += sum(i)
    Min = min(Min, min(i))
print(Sum - (Min * (h * w)))
