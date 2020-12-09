k = int(input())
a, b = map(int, input().split())
if a > b:
    print("NG")
if a == b:
    if b % k == 0:
        print("OK")
        exit()
    else:
        print("NG")
        exit()
num_a = a // k
num_b = b // k
if num_b > num_a:
    print("OK")
else:
    if a % k == 0:
        print("OK")
    else:
        print("NG")
