from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
d = []

# 1. 따옴표(.)를 기준으로 문자열을 나눈 후 확장자를 리스트에 저장
for i in range(n):
    _, ext = input().rstrip().split('.')
    d.append(ext)

# 2. Counter로 리스트의 각 요소가 몇번씩 사용되었는지 받아온 후 정렬
for k, v in sorted(Counter(d).items()):
    print(f"{k} {v}")