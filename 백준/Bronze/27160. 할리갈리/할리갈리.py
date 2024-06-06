import sys
input = sys.stdin.readline


# 1. 값를 입력받고 과일key:개수를 저장
def read_input(num):
    fruit_counts = {}
    for _ in range(num):
        fruit, cnt = input().split()
        fruit_counts[fruit] = fruit_counts.get(fruit, 0) + int(cnt)
    return fruit_counts


# 2. 5개가 된 과일이 있는지 체크
def check_fruit_count(fruit_counts):
    return 'YES' if 5 in fruit_counts.values() else 'NO'


def main():
    num = int(input().rstrip())
    fruit_counts = read_input(num)
    result = check_fruit_count(fruit_counts)
    print(result)


if __name__ == "__main__":
    main()
