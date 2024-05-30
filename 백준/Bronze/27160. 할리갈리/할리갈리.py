c = int(input())
d = {}

# 1. 입력값만큼 for문을 돌면서 딕셔너리에 과일key:개수를 저장 
for i in range(c):
    t, n = input().split()
    d[t] = d.get(t, 0) + int(n)

# 2. value값으로 딕셔너리를 리스트로 변환 -> 5가 있는지 체크
if 5 in list(d.values()):
    print('YES')
else:
    print('NO')
