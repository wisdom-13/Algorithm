import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

PN = "IO" * N + "I"
pn_len = len(PN)
chk = 0

for i in range(M):
    if S[i:i+pn_len] == PN:
        chk += 1

print(chk)
