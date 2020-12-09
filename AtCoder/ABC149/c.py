def prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

x = int(input())
while prime(x) == False:
    x += 1
print(x)
