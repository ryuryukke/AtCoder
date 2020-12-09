# k = int(input())
# if k % 2 == 0:
#     print(-1)
#     exit()
k = int(input())
# あまりはループする。したがって最大で、k回までみて、なかったら-1出力する感じで。
surps = dict()
num = 7
while 1:
    surp = num % k
    if surp == 0:
        print(len(str(num)))
        exit()
    else:
        if surp in surps:
            print(-1)
            exit()
        else:
            surps[surp] = 1
            num = (num * 10 + 7) % k





