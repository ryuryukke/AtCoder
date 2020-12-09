# この問題はc問題と比べて特段解きやすかった。
N = int(input())
A = tuple(map(int, input().split()))
M = [-1] * N
acc = 0
for i in range(1, N, 2):
    acc += A[i]
acc *= 2
M[0] = sum(A) - acc
for i in range(N-1):
    M[i+1] = 2*A[i] - M[i]
print(*M)