# import itertools
# n = int(input())
# l = list(map(int, input().split()))
# nums = [i for i in range(len(l))]
# ans = 0
# for ptr in itertools.combinations(nums, 3):
#     table = dict()
#     cand = []
#     for j in ptr:
#         table[j] = l[j]
#         cand.append(l[j])
#     if len(set(cand)) == 3:
#         k = sorted(table.items(), key=lambda x:x[1])
#         if k[2][1] < k[0][1] + k[1][1]:
#             ans += 1
# print(ans)

n = int(input())
l = tuple(map(int, input().split()))
table = dict()
ans = []
for i, v in enumerate(l):
    table[v] = i
for i in range(len(l)-2):
    for j in range(i+1, len(l)-1):
        a, b = l[i], l[j]
        if a == b:
            continue
        else:
            cand = [v for v, k in table.items() if a + b > v and j < k]
            for num in cand:
                ans.append((a,b,num))
print(ans)
            


        

    
    