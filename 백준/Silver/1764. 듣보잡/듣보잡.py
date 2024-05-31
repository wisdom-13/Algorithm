import sys
input = sys.stdin.readline

a_num, b_num = input().rstrip().split()
a_set = set()
b_set = set()

# 1. 듣도 못한 사람과 보도 못한 사람을 각각 set에 저장
for _ in range(int(a_num)):
    a_set.add(input().rstrip())

for _ in range(int(b_num)):
    b_set.add(input().rstrip())

# 2. 두 set의 합집합을 정렬
ab_set = sorted(a_set & b_set)

print(len(ab_set))
print(*ab_set, sep='\n')  # *:unpacking
