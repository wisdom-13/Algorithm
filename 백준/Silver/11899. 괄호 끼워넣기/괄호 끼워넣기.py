import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []
cnt = 0
for c in S:
    if c == '(':
        stack.append(c)
    else:
        if not stack:
            cnt += 1
        else:
            stack.pop()

print(len(stack) + cnt)
