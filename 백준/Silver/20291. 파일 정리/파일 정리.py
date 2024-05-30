from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
d = []

for i in range(n):
    _, ext = input().rstrip().split('.')
    d.append(ext)

# Counter를 정렬
for k, v in sorted(Counter(d).items()):
    print(f"{k} {v}")
