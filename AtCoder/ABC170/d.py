from math import gcd
from collections import defaultdict

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    times = defaultdict(int)
    for i in a:
        times[i] += 1
    for j in a:
        # 元の数列に重複がある場合の処理
        if times[j] > 1:
            continue
        tmp = set(a)
        tmp.remove(j)
        table_ = make_divisors(j)
        for i in table_:
            if i in tmp:
                break
        else:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
