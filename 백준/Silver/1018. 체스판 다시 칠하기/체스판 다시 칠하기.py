import sys
input = sys.stdin.readline

caseA = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]


# 0. 두개의 2차원 배열을 비교 > 일치하지 않는 요소 값을 return
def compare(A, B):
    num = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if (B[i][j] == A[i][j]):
                num += 1
    return int(num)


y, x = map(int, input().rstrip().split())
cnt_list = []

grid = [list(input().rstrip()) for _ in range(y)]

# 1. 가로 세로를 한칸씩 옮겨가면서 만들 수 있는 8x8 사이즈의 배열을 만들기
# 2. 만들어진 8x8 배열을 caseA, caseB와 비교해서 일치하지 않는 요소의 개수를 배열에 저장
#    (64 - caseA와 일치하지 않는 개수 = caseB와 일치하지 않는 개수)
for i in range(y - 7):
    for j in range(x - 7):
        new_grid = [row[j:j+8] for row in grid[i:i+8]]
        new_grid_cnt = compare(caseA, new_grid)
        cnt_list.append(min(new_grid_cnt, 64 - new_grid_cnt))

# 3. 가장 작은 값 출력
print(min(cnt_list))
