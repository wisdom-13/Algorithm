import sys
input = sys.stdin.readline


# 특정 높이값일때 얻을 수 있는 나무의 수
def get_wood(wood_list, height):
    return sum(x - height for x in wood_list if x > height)


def main():
    N, M = map(int, input().rstrip().split())
    wood_list = list(map(int, input().rstrip().split()))

    low, high = 0, max(wood_list)
    result = 0

    # 이분탐색
    while low <= high:
        mid = (low + high) // 2
        wood = get_wood(wood_list, mid)

        if wood >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)


if __name__ == "__main__":
    main()
