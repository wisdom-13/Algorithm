import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
num_list = []
num = 1

while len(num_list) < B:
    num_list += [num] * num
    num += 1

print(sum(num_list[A-1:B]))