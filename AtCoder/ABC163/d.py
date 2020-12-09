# n, k = map(int, input().split())
# n = n + 1
# MOD = 10**9 + 7
# sum = 0
# def comb(s,e):
# 	comb1 = 1
# 	for i in range(s-e+1,s+1): # n*(n-1)*(n-2)*...*(n-a+1)(mod p)を計算
# 		comb1 *= i
# 		comb1 %= MOD
# 	for i in range(1,e+1): # 1/a!(mod p)を計算 フェルマーの小定理:1/a = a^p-2(mod p)を利用
# 		comb1 *= pow(i,MOD-2,MOD)
# 		comb1 %= MOD
# 	return comb1

# for i in range(k, n):
# 	if i >= n//2:
# 		sum += comb(n, n-i)
# 	else:
# 		sum += comb(n, i)
# print(sum%MOD)
N, K = map(int, input().split())
MOD = 10**9+7
ans = 0
for i in range(K, N+2):
	ans += i*(N-i+1)+1
	ans %= MOD
print(ans%MOD)

# fact = [0] * (N+2)
# fact[0] = fact[1] = 1

# def comb_init():
# 	global fact
# 	for i in range(2, N+2):
# 		fact[i] = i * fact[i-1]

# def comb(n, r):
# 	global fact
# 	x = fact[n] % MOD
# 	y = pow(fact[r], -1, MOD)*pow(fact[n-r], -1, MOD)
# 	return (x*y)%MOD

# ans = 0
# comb_init()
# for i in range(K, N+2):
# 	ans += comb(N+1, i)
# 	ans %= MOD
# print(ans%MOD)


