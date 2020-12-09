from collections import defaultdict
h, w, m = map(int, input().split())
hw = [tuple(map(int, input().split())) for _ in range(m)]
tate, yoko = defaultdict(int), defaultdict(int)
for h, w in hw:
    tate[h] += 1
    yoko[w] += 1
tate = sorted(tate.items(), key=lambda x:x[1], reverse=True)
yoko = sorted(yoko.items(), key=lambda x:x[1], reverse=True)
tate_max, yoko_max = tate[0][1], yoko[0][1]
max_tates, max_yokos = [], []
for t in tate:
    if t[1] == tate_max:
        max_tates.append(t)
    else:
        break
for y in yoko:
    if y[1] == yoko_max:
        max_yokos.append(y)
    else:
        break
hw = set(hw)
for ta in max_tates:
    for yo in max_yokos:
        if (ta[0], yo[0]) not in hw:
            print(tate_max + yoko_max)
            exit()
print(tate_max + yoko_max - 1)





