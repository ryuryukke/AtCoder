from collections import defaultdict
S = input()
t = defaultdict(int)
for i in S:
  t[i] += 1
if len(t.keys()) == 2:
  for i in t.values():
    if i != 2:
      print("No")
      break
  else:
    print("Yes")
else:
  print("No")