# import sys
# from collections import defaultdict
def main():
    # input = sys.stdin.readline
    n = int(input())
    # nums_table = defaultdict(int)
    nums_table = [2] * (n+1)
    ans = 0
    for i in range(1, n+1):
        nums_table[i] = 2
    nums_table[1] = 1
    for i in range(2, n//2+1):
        for j in range(2*i,n+1,i):
            nums_table[j] += 1
    for i in range(1, n+1):
        ans += i * nums_table[i]
    print(ans)
if __name__ == "__main__":
    main()
