# 포함 기준 수
n = int(input())
# n이 포함되지 않은 시간 개수
result = 0

# 60분과 60초 중에서
for i in range(60):
    # 십의자리와 일의 자리에 n이 들어있지 않으면
    if (i % 10 != n) & (i // 10 != n):
        # result 증가
        result += 1
# n까지의 모든 시간 중에서 n이 1개도 들어있지 않는 숫자 빼기
result = (n+1) * 60 * 60 - result * result * n
# 출력ㅗ
print(result)