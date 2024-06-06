import sys
input = sys.stdin.readline

N = input().rstrip().split()
N_list = list(map(int, input().rstrip().split()))
N_dict = {item: 1 for item in N_list}

M = input().rstrip().split()
M_list = map(int, input().rstrip().split())

for i in M_list:
    print(N_dict.get(i, 0))
