"""
arr = [국가, 금, 은, 동]
정렬: lambda 이용해서 금, 은, 동 순
출력: 앞에꺼랑 다르면 등수가 맞음 같으면 앞이랑 같은 등수
"""

nation, want = map(int, input().split(" "))

arr = [[0 for j in range(4)] for i in range(nation)]
for i in range(nation):
       arr[i] =  list(map(int, input().split()))
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
var=0
for i in range(nation):
    # 찾으면
    if arr[i][0] == want:
        print(i+1 -var)
    else:
        # 뒤에꺼랑 비교
        if i!=nation-1 and arr[i][1] == arr[i + 1][1] and arr[i][2] == arr[i + 1][2] and arr[i][3] == arr[i + 1][3]:
            var += 1
        else:
            var = 0
