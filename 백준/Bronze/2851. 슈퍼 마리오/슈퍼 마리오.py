import sys
input = sys.stdin.readline

total = 0
answer = 0
mushroom = []

for _ in range(10):
    mushroom.append(int(input().rstrip()))

for i in mushroom:
    prev_tatal = total
    total = total + i

    # 총합이 100을 넘기면 이전 값과 비교해서 차이가 적은 것을 출력
    if (total >= 100):
        if abs(100 - total) <= abs(100 - prev_tatal):
            answer = total
        else:
            answer = prev_tatal
        break

print(answer if answer else total)
