# 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬하기
data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

# 계산하기
result=0
result += count * first
result += (m-count) * second

# 출력하기
print(result)
