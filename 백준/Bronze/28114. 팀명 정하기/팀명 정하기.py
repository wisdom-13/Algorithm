import sys
input = sys.stdin.readline


# 1. 입학 연도기준
def year_team_name(year_list):
    return "".join(map(str, sorted(year_list)))


# 푼 문제수 기준
def solved_team_name(solved_list):
    sort_list = sorted(solved_list, reverse=True)
    return "".join([char for _, char in sort_list])


def main():

    year_list = []
    solved_list = []
    for _ in range(3):
        solved, year, name = input().rstrip().split()
        year_list.append(int(year) % 100)
        solved_list.append((int(solved), name[0]))

    print(year_team_name(year_list))
    print(solved_team_name(solved_list))


if __name__ == "__main__":
    main()
