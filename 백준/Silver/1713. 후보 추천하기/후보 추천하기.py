from collections import deque
import sys
input = sys.stdin.readline


N = int(input().rstrip())  # 사진틀
M = int(input().rstrip())  # 학생수
vote_list = list(map(int, input().rstrip().split()))
phote_list = {}


# 번호 : 득표수 형태로 딕셔너리에 저장
# 이미 사진틀에 등록되어 있거나 사진틀에 자리가 있으면 투표수 + 1
# 자리가 없으면 가장 득표수가 낮고 오래된 사진을 삭제

for student in vote_list:

    voto_num = phote_list.get(student, 0)
    if voto_num != 0 or len(phote_list) < N:
        phote_list[student] = voto_num + 1

    else:
        # value의 최솟값의 key
        delete_key = min(phote_list, key=phote_list.__getitem__)
        del phote_list[delete_key]
        phote_list[student] = voto_num + 1


print(*sorted(phote_list.keys()))
