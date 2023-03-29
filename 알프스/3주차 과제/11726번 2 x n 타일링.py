#bottom-up

# 입력받기
n = int(input())
arr = [0 for _ in range(1000)]
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
    arr[i] = arr[i - 2] + arr[i - 1]

# 큰 타일이 최대로들어가는 개수 구하기
result = arr[n] % 10_007
print(result)


#top-down

import sys
sys.setrecursionlimit(10 ** 6)
dp = [0] * 1001
def f(x):
    if x <=1:
        return 1
    if dp[x] > 0:
        return dp[x]
    dp[x] = (f(x-2) + f(x-1)) % 10007
    return dp[x]


n = int(input())
print(f(n))
