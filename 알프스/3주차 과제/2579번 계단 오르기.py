# 전체 개수 입력받기
n = int(input())
# 각 계단의 점수를 저장할 배열 0으로 초기화
arr = [0] * (n+2) # n+2를 한 이유는 밑에서 visit[2] = arr[1] + arr[2] 이 작업을 할 때 최소 길이 3의 배열이 필요하기 때문이다.
# 계단의 점수를 arr 배열에 저장
for i in range(n):
    arr[i+1] = (int(input()))
# 각 계단이 마지막 계단일 때 최대 점수를 저장할 배열 초기화
visit = [0] * (n+2)
# visit 배열의 1번째와 2번째 값 저장
visit[1] = arr[1]
visit[2] = arr[1] + arr[2]
# 반복문을 돌며 visit[x] 값 구하기
for x in range(3, n+1):
    visit[x] = max(visit[x - 3] + arr[x - 1], visit[x - 2]) + arr[x]
# 정답 출력
print(visit[n])
