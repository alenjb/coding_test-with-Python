columns, rows = map(int, input().split())
# 2차원 배열로 입력받기
data = [list(map(int, input().split()))for _ in range(columns)]
# 각 행에서 제일 작은 수 중에 제일 큰 수
min_num = 0
# 모든 행을 돌면서
for i in range(len(data)):
    # 제일 작은 수가 이전의 작은 수보다 크면 그것을 min_num에 담기
    if min_num < min(data[i]):
        min_num = min(data[i])
# 출력
print(min_num)
