n = int(input())
three = [3]
five = [5]
num, num_ = 0, 0
while num < 10**18:
    num = three[-1] * 3
    three.append(num)
while num_ < 10**18:
    num_ = five[-1] * 5
    five.append(num_)
for i, v in enumerate(three):
    for i_, v_ in enumerate(five):
        if v + v_ == n:
            print(i+1, i_+1)
            exit()
print(-1)