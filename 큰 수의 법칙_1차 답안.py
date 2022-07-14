# 입력받기
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# 큰 수와 두번째로 큰 수 구하기
maxNum = max(arr)
arr.remove(maxNum)
secondNum = max(arr)

# 계산하기
addNum = m//k
addNum2 = addNum-1
value = secondNum* addNum2 + maxNum * addNum*k
if m - (addNum2+addNum*k) != 0:
  value += (m - (addNum2+addNum*k)) * secondNum

# 출력하기
print(value)
