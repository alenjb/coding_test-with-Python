import sys
total, itnum = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))
sumArr=[0]
temp = 0
for i in arr:
    temp += i
    sumArr.append(temp)
for i in range(itnum):
    a, b = map(int, input().split())
    print(sumArr[b] - sumArr[a-1])
