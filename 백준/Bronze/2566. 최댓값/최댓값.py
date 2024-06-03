import sys
input = sys.stdin.readline

max_num, max_row, max_col = 0, 0, 0

grid = [list(map(int, input().rstrip().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if max_num <= grid[i][j]:
            max_num = grid[i][j]
            max_row = i+1
            max_col = j+1

print(max_num)
print(max_row, max_col)
