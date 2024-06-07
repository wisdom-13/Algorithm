import sys
input = sys.stdin.readline


N = input().rstrip()
X = list(map(int, input().rstrip().split()))

# 1. 중복 제거 후 정렬
sorted_X = sorted(set(X))

# 2. 값:순서 형식의 딕셔너리 생성
dict_X = {v: i for i, v in enumerate(sorted_X)}

# 3. 값으로 딕셔너리를 조회해서 출력
print(*[dict_X[v] for v in X])
