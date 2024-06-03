import sys
input = sys.stdin.readline

grid = [list(input().rstrip()) for _ in range(5)]
new_list = [''] * 15

for entry in enumerate(grid):
    i, v = entry
    for j in range(len(v)):
        new_list[j] += grid[i][j]

print("".join(new_list))
