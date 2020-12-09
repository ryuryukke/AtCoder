n = int(input())
ans = set()
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        ans.add(i)
        ans.add(n//i)
for num in sorted(list(ans)):
    print(num)
