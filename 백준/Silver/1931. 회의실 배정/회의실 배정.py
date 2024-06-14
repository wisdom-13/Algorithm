import sys
input = sys.stdin.readline

N = int(input().rstrip())
meetings = []

for _ in range(N):
    start, end = map(int, input().rstrip().split())
    meetings.append((start, end))

# 끝나는 시간 / 시작 시간으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)
