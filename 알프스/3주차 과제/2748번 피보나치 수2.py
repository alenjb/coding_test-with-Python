# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    arr = []
    for i in range(n+1):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-2]+arr[i-1])
    return arr[n]


n = int(input())
result = fibonacci(n)
print(result)