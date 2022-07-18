# 총 이동 횟수
n = int(input())
# 명령어 집합
arr = list(input().split())
# x좌표와 y좌표 시작값은 1
x = 1
y = 1
# 리스트에서 하나씩 꺼내서 각 조건에 맞으면 동작
for i in arr:
    if (i == 'R') & (x < n):
        x += 1
    elif (i == 'L') & (x > 1):
        x -= 1
    elif (i == 'U') & (y > 1):
        y -= 1
    elif (i == 'D') & (y < n):
        y += 1
# 결과 출력
print(y, x)
