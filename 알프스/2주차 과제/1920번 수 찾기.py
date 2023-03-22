
def find(x, start, end):
    mid = (start + end) // 2
    if end - start < 0:
        print(0)
    elif sList1[mid] == x:
        print(1)
    elif sList1[mid] > x:
        return find(x, 0, mid-1)
    elif sList1[mid] < x:
        return find(x,  mid + 1, len(sList1)-1)


m = int(input())
list1 = list(map(int, input().split()))

n = int(input())
list2 = list(map(int, input().split()))

sList1 = sorted(list1)
for i in list2:
    find(i, 0, len(sList1)-1)
