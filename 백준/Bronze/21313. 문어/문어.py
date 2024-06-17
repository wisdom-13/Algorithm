import sys
input = sys.stdin.readline

# 문어가 짝수일 경우 : 1212 반복
# 문어가 홀수일 경우 : 1212 반복 후 마지막에 3 추가

N = int(input().rstrip())
num_list = [1, 2] * (N // 2)

if N % 2 == 1:
    num_list.append(3)

print(*num_list)
