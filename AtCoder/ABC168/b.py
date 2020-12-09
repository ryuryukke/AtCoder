k = int(input())
s = input()
if len(s) <= k:
    print(s)
    exit()
else:
    print(s[:k]+"...")
    exit()
