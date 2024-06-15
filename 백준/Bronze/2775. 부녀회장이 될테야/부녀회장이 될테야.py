import sys
input = sys.stdin.readline

T = int(input().rstrip())
k_list = []  # 층
n_list = []  # 호

for _ in range(T):
    k_list.append(int(input().rstrip()))
    n_list.append(int(input().rstrip()))

max_k, max_n = max(k_list), max(n_list)


# 최대 층, 최대 호까지의 사람 수를 저장
apart = [[0] * (max_n + 1) for _ in range(max_k + 1)]
apart[0] = [i for i in range(max_n + 1)]  # 0층 초기화

for i in range(1, max_k+1):
    for j in range(1, max_n+1):
        apart[i][j] = sum(apart[i-1][:j+1])  # 이전층의 j호 까지 사람의 합

# k층 n호의 사람 출력
for i in range(T):
    print(apart[k_list[i]][n_list[i]])