L, R = map(int, input().split())
# もう少し全探索を疑うことが大切。
if R - L >= 2019:
    print(0)
else:
    # なぜprint(L*(L+1)%2019)が不可なのかというと、2019が2019=3*673の合成数であるから。
    # だから取りうる最小と最小+1の積の2019MODが最小になるわけではない。
    # 加えて、かけるものどうしの余剰が最小であれば、その積の余剰も最小になるという前提が間違っている。
    ans = float("inf")
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j)%2019)
    print(ans)