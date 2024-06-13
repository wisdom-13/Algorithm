import sys
input = sys.stdin.readline

def solution(command_list):
    direction = 0  # 북(0), 동(1), 남(2), 서(3)
    pos = [0, 0]

    routeX = [0]
    routeY = [0]

    for command in command_list:
        if command == "L":
            direction = (direction - 1) % 4
        elif command == "R":
            direction = (direction + 1) % 4
        elif command == "F":
            pos[0] += dx[direction]
            pos[1] += dy[direction]
        elif command == "B":
            pos[0] -= dx[direction]
            pos[1] -= dy[direction]

        routeX.append(pos[0])
        routeY.append(pos[1])

    return (max(routeX) - min(routeX)) * (max(routeY) - min(routeY))

move = {"F": 1, "B": -1}
# 북, 동, 남, 서 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input().rstrip())

for _ in range(T):
    command_list = list(input().rstrip())
    print(solution(command_list))
