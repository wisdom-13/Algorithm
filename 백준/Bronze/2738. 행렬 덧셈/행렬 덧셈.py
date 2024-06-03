import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 1. M * N의 이차원 리스트 생성
list = [[0] * M for _ in range(N)]

# 2. A 행렬의 값을 리스트에 저장
for i in range(N):
    A_list = input().rstrip().split()
    for j in range(M):
        list[i][j] = int(A_list[j])

# 3. B 행렬의 값을 기존 리스트의 값에 더하여 자장
for i in range(N):
    B_list = input().rstrip().split()
    for j in range(M):
        list[i][j] = list[i][j] + int(B_list[j])

# 4. 출력
for i in list:
    for j in i:
        print(j, end=" ")
    print()
