# n과 k 입력받기
n, k = map(int, input().split())
# 결과를 저장할 변수
result = 0
# n이 1이 될 때까지 반복
while n != 1:
    # n이 k로 나누어 떨어지면
    if n % k == 0:
        n = n / k
        result += 1
    # n이 k로 나누어 떨어자지 않으면
    else:
        n -= 1
        result += 1
# 결과 출력
print(result)