a, b, c = map(int, input().split())
print((100-a)*(a/(a+b+c)) + (100-b)*(b/(a+b+c)) + (100-c)*(c/(a+b+c)))