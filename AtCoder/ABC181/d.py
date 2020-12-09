from collections import defaultdict
s = input()
lst = [i*8 for i in range(13, 125)]
exist = defaultdict(int)
for st in s:
    exist[st] += 1
cache = dict()
for i in lst:
    cache[i] = list(str(i))
if int(s) < 100:
    if int(s) % 8 == 0:
        print("Yes")
        exit()
    else:
        if int(s[-1]+s[0]) % 8 == 0:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
else:
    for i, v in cache.items():
        tmp = exist.copy()
        for j in v:
            if j in tmp:
                if tmp[j] == 0:
                    break                    
                tmp[j] -= 1
            else:
                break
        else:
            print("Yes")
            exit()
    print("No")
        
        
    

        
