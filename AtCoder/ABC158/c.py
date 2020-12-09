a, b = map(int, input().split())
min_a = a//0.08
max_a = (a+1)//0.08
min_b = b//0.1
max_b = (b+1)//0.1
a_array = set(range(int(min_a)+1, int(max_a)))
b_array = set(range(int(min_b)+1, int(max_b)))
common = a_array & b_array
print("-1" if len(common) == 0 else min(common))
