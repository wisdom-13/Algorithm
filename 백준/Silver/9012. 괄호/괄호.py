import sys
input = sys.stdin.readline

num = int(input().rstrip())
answer = []

# 1. chk에 ( 는 +1 )는 -1
# 2. chk 값이 -가 되면 바로 탈락
# 3. 올바른 괄호는 chk 가 0이 되어야함
for i in range(num):
    chk = 0
    arr = list(input().rstrip())
    for j in arr:

        if j == "(":
            chk += 1
        elif j == ")":
            chk -= 1

        if chk < 0:
            break

    answer.append("YES" if chk == 0 else "NO")

print(*answer, sep="\n")
