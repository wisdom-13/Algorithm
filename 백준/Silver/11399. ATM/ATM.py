import sys
input = sys.stdin.readline


def waiting_time(people):
    sort_people = sorted(people)

    waiting_list = [0]
    for time in sort_people:
        waiting = time + waiting_list[-1]
        waiting_list.append(waiting)

    return sum(waiting_list)


def main():
    N = input().rstrip()
    people = map(int, input().rstrip().split())
    print(waiting_time(people))


if __name__ == "__main__":
    main()
