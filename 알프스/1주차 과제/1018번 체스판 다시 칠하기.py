m, n = map(int, input().split())
row, col = 0
arr = [[0 for i in range(50)] for i in range(50)]
for i in range(50):
    if arr[i] == 0:
        row = i
        break
    for j in range(50):
        if arr[j] == 0:
            col =j
            break
        arr[i][j] = int(input())
for i in range(0, row-n):
    for j in range(0, )