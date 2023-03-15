testCase = int(input())

for i in range(testCase):
    num = list(map(int, input().split()))
    print(min(num))