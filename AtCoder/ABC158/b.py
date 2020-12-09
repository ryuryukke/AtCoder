# divmod : 商と余りのタプルを返す組み込み関数
n, a, b = map(int,input().split())
q, r = divmod(n, a+b)
print(a*q+a if r >= a else a*q+r)
