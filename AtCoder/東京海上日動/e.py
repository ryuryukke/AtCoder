import itertools
n, k, s, t = map(int, input().split())
a = list(map(int, input().split()))
table = dict()
for v in a:
    table[v] = [0] * 18
    for i in range(18):
        if v>>i & 1:
            table[v][17-i] = 1
ans = 0
for pattern in itertools.product([0, 1], repeat=n):
    if 1 not in pattern:
        continue
    ans_s = 0
    ans_t = 0
    s_ = [False] * 18
    t_ = [True] * 18
    for i, v in enumerate(pattern):
        if v == 1:
            for index, l in enumerate(table[a[i]]):
                if l == 1:
                    s_[index] = True
                else:
                    t_[index] = False
    for k, v in enumerate(s_):
        if v == True:
            ans_s += 2**(18-k-1)
    for n, v in enumerate(t_):
        if v == True:
            ans_t += 2**(18-n-1)
    if ans_s == s and ans_t == t:
        ans += 1
print(ans)


