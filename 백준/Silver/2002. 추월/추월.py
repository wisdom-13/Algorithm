import sys
input = sys.stdin.readline

num = int(input().rstrip())
chk = 0
in_list = []
out_list = set()


# 1. 들어간 차량을 '차량번호:순서' 형태로 저장
for i in range(num):
    in_list.append(input().rstrip())

for j in range(num):
    out_car = input().rstrip()
    # 2. 먼저 들어간 차량 리스트
    front_list = in_list[0:in_list.index(out_car)]

    # 3. 먼저 들어간 차량 리스트 - 먼저 나온 차량 리스트 > 0 : 추월
    if len(set(front_list) - out_list):
        chk += 1

    out_list.add(out_car)

print(chk)
