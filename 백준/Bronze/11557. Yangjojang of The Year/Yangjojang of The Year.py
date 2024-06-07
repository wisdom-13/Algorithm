import sys
input = sys.stdin.readline


# 술 소비량:학교이름으로 딕셔너리에 저장
# 술 소비량을 리스트에 저장한 후 최대값으로 학교이름 return
def best_drinker(num):
    school_list = {}
    cnt_list = []
    for _ in range(num):
        school, cnt = input().rstrip().split()
        school_list[int(cnt)] = school
        cnt_list.append(int(cnt))

    return school_list[max(cnt_list)]


def main():
    case = int(input().rstrip())

    for _ in range(case):
        num = int(input().rstrip())
        school = best_drinker(num)
        print(school)


if __name__ == "__main__":
    main()
