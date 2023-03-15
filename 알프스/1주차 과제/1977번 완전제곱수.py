import math

m = int(input())
n = int(input())

list1 = []
for i in range(m, n+1):
    if math.sqrt(i) == float(int(math.sqrt(i))):
        list1.append(i)
if list1:
    print(sum(list1))
    print(list1[0])
else:
    print(-1)
