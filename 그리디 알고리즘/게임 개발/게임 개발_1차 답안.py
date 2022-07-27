#
# # left 함수
# ex) (3,2)  ->  arr[2][3]
def left_check(a):
    if (a == 0) & (x > 0):
        return arr[y][x - 1]
    elif (a == 1) & (y > 0):
        return arr[y - 1][x]
    elif (a == 2) & (x < n):
        return arr[y][x + 1]
    elif (a == 3) & (y < m):
        return arr[y + 1][x]


def left(x1, y1, d1, arr1):
    if (d1 == 0) & (x > 0):
        arr[y1][x1 - 1] = 2
        x1 = x1 - 1
    elif (d1 == 1) & (y > 0):
        arr[y1 - 1][x1] = 2
        y1 = y1 + 1
    elif (d1 == 2) & (x < n):
        arr[y1][x1 + 1] = 2
        x1 = x1 + 1
    elif (d1 == 3) & (y < m):
        arr[y1 + 1][x1] = 2
        y1 = y1 - 1
    return x1, y1, d1, arr1

# ex) (3,2)  ->  arr[2][3]


def right(x2, y2, d2):

    if d2 == 0:
        if arr[y2][x2+1] == 1:
            return 0
        x2 = x2+1

    elif d2 == 1:
        if arr[y2+1][x2] == 1:
            return 0
        y2 = y2+1

    elif d2 == 2:
        if arr[y2][x2-1] == 1:
            return 0
        x2 = x2-1

    elif d2 == 3:
        if arr[y2-1][x2] == 1:
            return 0
        y2 = y2 - 1


# 입력 받기(n=세로, m=가로)
n, m = map(int, input().split())
x, y, d = map(int, input().split())
# 현재 위치에서 몇번의 방향을 확인 했는지
check = 0
# 총 이동한 횟수
move = 0

# 맵 만들기
arr = []
for i in range(n):
     arr.append(list(map(int, input().split())))
# 첫 위치는 다녀갔으므로 2로 지정
arr[y][x] = 2
# 총 이동 횟수도 증가
move += 1

# 방향 리스트 - 북-서-남-동
direction = [0, 3, 2, 1]
while True:
    # 4방향을 다 확인했으면
    if check == 4:
        # 오른쪽이 바다이면
        if right(x, y, d) == 0:
            # 현재 위치와 총 움직인 횟수를 출력
            print("끝", y, x, move)
            break
        else:
            # 오른쪽(뒤쪽)이 바다가 아니면 한칸 뒤로 가기
            right(x, y, d)
            check = 0

# 왼쪽부터 확인 0->3->2->1->0
# 방향 바꾸기
    # 방향이 동쪽이면
    if d == 1:
        d = 0
    # 동쪽 이외의 방향이면
    else:
        d = direction[direction.index(d)+1]

    # 가본지 확인(가봤으면 2 / 안가봤으면 0)
    if left_check(d) == 2:
        check += 1
        print(d,"방향 체크함 ", check)
        continue
    elif left_check(d) == 0:
        # 이동
        x, y, d, arr = left(x, y, d, arr)
        move += 1
        print("현재 방향: ", d)
        print("현재 좌표", y, x)
        print("현재 체크한 횟수", check)
        print("현재 움직인 횟수", move)
        for k in range(len(arr)):
            print(arr[k])
        print("--------------------------------")
