import sys
input = sys.stdin.readline

direction = {
    "R": [1, 0],
    "L": [-1, 0],
    "B": [0, -1],
    "T": [0, 1],

    "RT": [1, 1],
    "LT": [-1, 1],
    "RB": [1, -1],
    "LB": [-1, -1],
}


def posToNum(pos):
    x, y = list(pos)
    x = ord(x) - 65
    return [x, int(y) - 1]


def numToPos(num):
    x, y = num
    x = chr(x + 65)
    return x + str(y+1)


K, D, N = input().rstrip().split()

k_pos = posToNum(K)
d_pos = posToNum(D)

for _ in range(int(N)):
    move = direction[input().rstrip()]

    # 이동 후 위치가 맵을 벗어나지 않으면 킹을 새로운 위치로 이동
    if all(0 <= num <= 7 for num in [k_pos[0] + move[0], k_pos[1] + move[1]]):
        new_k_pos = [k_pos[0] + move[0], k_pos[1] + move[1]]

        # 새로운 위치에 돌이 있을 경우 돌을 같은 방향으로 이동 / 돌의 위치가 맵을 벗어나지 않으면 값 업데이트
        if new_k_pos[0] == d_pos[0] and new_k_pos[1] == d_pos[1]:
            if all(0 <= num <= 7 for num in [d_pos[0] + move[0], d_pos[1] + move[1]]):
                d_pos = [d_pos[0] + move[0], d_pos[1] + move[1]]
                k_pos = new_k_pos
        else:
            k_pos = new_k_pos


print(numToPos(k_pos))
print(numToPos(d_pos))
