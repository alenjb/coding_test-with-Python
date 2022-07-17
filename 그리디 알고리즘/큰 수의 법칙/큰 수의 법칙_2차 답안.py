# 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬하기
data.sort()
first=data[n-1]
second=data[n-2]

# 한 단위의 합
bound= first * k + second

# 계산하기
value = (m//(k+1)) * (bound) + m % (k+1) * first

# 출력하기
print(value)
