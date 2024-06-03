import sys
input = sys.stdin.readline

num = int(input().rstrip())
x = []
y = []
line = []

# 0. 리스트에서 특정 index의 앞 뒤 요소의 차
def diff(list, index):
    next = list[index + 1] if len(list) > index + 1 else list[0]
    prev = list[index - 1] if len(list) > index - 1 else list[-1]
    return abs(int(next - prev))

# 1. 가장 큰 변의 길이를 구해서 전체 사각형의 크기 구하기
# 2. 작은 사각형의 크기 구하기 (작은 변의 길이는 가장 큰 변의 길이의 인접한 두 변의 차)
for i in range(6):
    way, size = map(int, input().rstrip().split())
    line.append(size)
    if (way in [1, 2]):
        x.append(size)
    else:
        y.append(size)

sx = diff(line, line.index(max(x)))
sy = diff(line, line.index(max(y)))

area = max(x) * max(y) - sx*sy

print(area * num)