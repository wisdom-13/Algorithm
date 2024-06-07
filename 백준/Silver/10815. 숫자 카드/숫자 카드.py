import sys
input = sys.stdin.readline


# 이분탐색
def have_card(card_list, card):
    low, high = 0, len(card_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if card_list[mid] == card:
            return 1
        if card_list[mid] < card:
            low = mid + 1
        else:
            high = mid - 1
    return 0


def main():
    input().rstrip()
    N_list = sorted(list(map(int, input().rstrip().split())))  # 상근이 보유
    input().rstrip()
    M_list = list(map(int, input().rstrip().split()))  # 비교대상

    result = []
    for i in M_list:  # i = 현재 비교할 카드
        result.append(have_card(N_list, i))

    print(*result)


if __name__ == "__main__":
    main()
