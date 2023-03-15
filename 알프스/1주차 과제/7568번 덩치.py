testCase = int(input())
Arr = []
Brr = []
arr = [1 for i in range (testCase)]
# 입력받기
for i in range(testCase):
    a, b = map(int, input().split())
    Arr.append(a)
    Brr.append(b)
# 분류하기
for i in range(testCase):
    for j in range(testCase):
        if (Arr[i] < Arr[j]) and (Brr[i] < Brr[j]):
            arr[i] += 1
print(*arr)

