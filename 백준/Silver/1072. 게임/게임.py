import sys
input = sys.stdin.readline


def change_rate(X, Y):
    Z = (Y * 100) // X

    # 승률이 절대 변하지 않는 경우
    if Z >= 99:
        return -1

    low, high = 0, 1000000000

    while low < high:
        mid = (low + high) // 2
        new_Z = ((Y + mid) * 100) // (X + mid)

        if new_Z > Z:
            high = mid
        else:
            low = mid + 1

    return low


# 입력 처리
X, Y = map(int, input().rstrip().split())
print(change_rate(X, Y))
