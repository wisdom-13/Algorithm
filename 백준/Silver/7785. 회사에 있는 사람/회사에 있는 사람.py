n = int(input())

# 1. 딕셔너리의 remove는 효율이 좋지 않기 때문에 set으로 선언
s = set()

# 2. enter일 경우 add 아닐경우 remove
for i in range(n):
    name, status = input().split()
    if status == 'enter':
        s.add(name)
    else:
        s.remove(name)

for j in sorted(s, reverse=True):
    print(j)
