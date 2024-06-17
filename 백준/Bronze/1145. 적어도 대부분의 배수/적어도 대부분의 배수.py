import sys
input = sys.stdin.readline


# 가장 작은 수 부터 배수 찾기 (나눠떨어지면 배수)
# 3개 이상이라면 출력
# 아니라면 1증가 후 반복 

num_list = list(map(int, input().rstrip().split()))
n = min(num_list)

while True:
    cnt = 0
    for i in num_list:
        if n % i == 0:
            cnt += 1

    if cnt >= 3:
        print(n)
        break

    n += 1
