import sys
input = sys.stdin.readline

plate = list(input().rstrip())
prev_plate = ''
height = 0

# 이전 그릇과 같다면 +5 다르다면 +10
for i in plate:
    height += 5 if i == prev_plate else 10
    prev_plate = i

print(height)