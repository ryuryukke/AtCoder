n = int(input())

def helper(num, sinhou):
    while num:
        if num % sinhou == 7:
            return False
        num //= sinhou
    return True

print(len([i for i in range(1, n+1) if helper(i, 10) and helper(i, 8)]))
