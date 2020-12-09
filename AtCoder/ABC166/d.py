x = int(input())
def judge(num):
    if num < 0:
        num *= -1
    ans = num**(1/5)
    if ans.is_integer():
        return True
    else:
        return False
if judge(x):
    if x < 0:
        print(-1*int(x**(1/5)), 0)
        exit()
    else:
        print(int(x**(1/5)), 0)
        exit()
b1 = 0
b2 = 0
while 1:
    b1 += 1
    b2 -= 1
    if judge(x+(b1**5)):
        print(int((x+(b1**5))**(1/5)), b1)
        exit()
    elif judge(x+(b2**5)):
        if x+(b2**5) < 0:
            print(-1*int(((x+(b2**5))*-1)**(1/5)), b2)
        else:
            print(int((x+(b2**5))**(1/5)), b2)
        exit()
