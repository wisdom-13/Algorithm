from heapq import heappush, heappop
import sys
input = sys.stdin.readline


A = list(input().rstrip())
B = list(input().rstrip())
number = []
new_number = []

for i in range(8):
    number.append(int(A[i]))
    number.append(int(B[i]))

# 숫자가 2개가 될때까지 반복
while len(number) > 2:
    for i in range(len(number) - 1):
        # 두 숫자의 합의 일의 자리
        new_number.append(str(int(number[i]) + int(number[i+1]))[-1])
    number = new_number
    new_number = []

print("".join(number))
