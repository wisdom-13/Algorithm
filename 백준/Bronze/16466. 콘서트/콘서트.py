import sys
input = sys.stdin.readline


# 1부터 시작해서 팔린 티켓 리스트에 있으면 +1 없으면 그 값을 return
def find_ticket(sold_tickets):
    sold_set = set(sold_tickets)
    i = 1
    while i in sold_set:
        i += 1
    return i


def main():
    int(input().rstrip())
    sold_tickets = list(map(int, input().rstrip().split()))
    print(find_ticket(sold_tickets))


main()
