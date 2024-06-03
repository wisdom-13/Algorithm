import sys
input = sys.stdin.readline

y, x = map(int, input().rstrip().split())
size = min(y, x)
answer = 0

grid = [list(input().rstrip()) for _ in range(y)]

# y가 1일 경우 무조건 1
if y == 1:
    print(1)
    exit()

# 1. x, y 중 작은 쪽이 최대 size / 반복하면서 size를 하나씩 --
# 2. 가로 세로를 한칸씩 옮겨가면서 모든 경우의 수의 size * size 크기 배열을 만들기
# 3. 배열의 각 모서리 값이 일치한다면 종료

while size >= 0:
    for i in range(y - (size-1)):
        if answer != 0:
            break

        for j in range(x - (size-1)):
            new_grid = [row[j:j+size] for row in grid[i:i+size]]

            if new_grid[0][0] == new_grid[0][-1] == new_grid[-1][-1] == new_grid[-1][0]:
                answer = size**2
                break
    size -= 1

print(answer)