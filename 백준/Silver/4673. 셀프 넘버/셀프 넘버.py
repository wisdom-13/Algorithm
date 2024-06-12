import sys
input = sys.stdin.readline


N = 10000

all_num = set([i for i in range(1, N+1)])
constructor = set()

# 1~1000까지 생성자 계산
for i in range(N+1):
    arr = list(map(int, str(i)))
    constructor.add(i + (i if len(arr) == 1 else sum(arr)))

# 1~ 1000 까지의 숫자중에 생성자가 있는 숫자 제외
print(*sorted(all_num - constructor), sep='\n')
