import sys
input = sys.stdin.readline

row, col = 0, 0
room = int(input().rstrip())

# 1. 문자열을 2차원 배열에 저장
grid = [list(input().rstrip()) for _ in range(room)]

# 2. 2차원 배열을 세로로 저장
h_grid = [''] * room
for entry in enumerate(grid):
    i, v = entry
    for j in range(len(v)):
        h_grid[j] += grid[i][j]

# 1. 가로 체크
#    배열을 문자열로 변환한 후 X를 기준으로 자름
#    잘린 문자열에 ..이 포함된다면 +1
for i in grid:
    for j in "".join(i).split("X"):
        if ".." in j:
            row += 1

# 2. 세로 체크
for i in h_grid:
    for j in "".join(i).split("X"):
        if ".." in j:
            col += 1

print(row, col)
