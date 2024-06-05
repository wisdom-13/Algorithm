import sys
input = sys.stdin.readline

num = int(input().rstrip())
list = [input().rstrip().split() for _ in range(num)]

# 배열의 순서를 뒤집어서 출력
for entry in enumerate(list):
    i, arr = entry
    print(f'Case #{i+1}: {" ".join(arr[::-1])}')