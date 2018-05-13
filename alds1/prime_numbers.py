n = int(input())
nums = [int(input()) for i in range(n)]
prime_num = 0

#フェルマーの小定理
def prime(n):
    q = abs(n)
    if q==2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

for i in nums:
    if(prime(i)): prime_num += 1

print(prime_num)
