
num = int(input())
arr = [0] * 10_001
for _ in range(1, num+1):
    arr[int(input())] += 1
for i in range(1, len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)