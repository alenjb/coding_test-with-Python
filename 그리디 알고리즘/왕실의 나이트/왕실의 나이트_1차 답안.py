# 데이터를 입력받음
input_str = input()
# 알파 리스트를 만들기
alpha = ['a', 'b','c', 'd', 'e', 'f', 'g']
# x좌표와 y죄표를 입력 데이터에서 슬라이싱하여 할당
x = int(alpha.index(input_str[0])+1)
y = int(input_str[1])
#움직일 수 있는 가지 수
result = 0
# ▷▷
if x < 7:
    # △
    if y < 8:
        result += 1
    # ▽
    if y > 1:
        result += 1
# ◁◁
if x > 2:
    # △
    if y < 8:
        result += 1
    # ▽
    if y > 1:
        result += 1
# ▽▽
if y < 7:
    # ▷
    if x < 8:
        result += 1
    # ◁
    if x > 1:
        result += 1
# △△
if y > 2:
    # ▷
    if x < 8:
        result += 1
    # ◁
    if x > 1:
        result += 1

print(result)