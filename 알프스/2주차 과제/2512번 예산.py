def bs(startNum, endNum, midNum):
    if startNum > endNum:
        return midNum
    cnt = 0
    mid = (startNum + endNum) //2
    # 모든 도시에 대해서 반복
    for i in arr:
        # 우리가 예측한 예산상한선보다 요구하는 예산이 많거나 같으면
        if i >= mid:
            # 최대 우리의 상한선까지만 배정
            cnt += mid
        # 우리가 예측한 예산상한선보다 요구하는 예산이 적으면
        else:
            cnt += i

    # 우리가 예측한 예산상한선에 따른 예산이 최대예산을 초과할 경우
    if cnt > limit:
        bs(0, mid-1, mid)
    else:
        bs(mid+1, end, mid)


n = int(input())
arr = list(map(int, input().split()))
limit = int(input())
start = 0
end = max(arr)
print(bs(start, end, (start + end) //2))


