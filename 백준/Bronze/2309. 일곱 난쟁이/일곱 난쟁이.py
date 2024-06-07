from itertools import combinations
import sys
input = sys.stdin.readline

l = []

for i in range(9):
    l.append(int(input().rstrip()))

for i in combinations(l, 7):
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break