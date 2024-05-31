
import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

c = int(input())
n = int(input())
result = 1

for i in range(n, 100):
    if ((A*i)+B > c*i):
        result = 0
        break

print(result)
