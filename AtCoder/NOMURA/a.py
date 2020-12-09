h1, m1, h2, m2, k = map(int, input().split())
whole = (h2-h1)*60+(60-m1)-(60-m2)
print(whole-k)
