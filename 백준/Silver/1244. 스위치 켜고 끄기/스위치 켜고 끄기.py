import sys
input = sys.stdin.readline

cnt = int(input().rstrip())
bulb = list(map(int, input().rstrip().split()))

student = int(input().rstrip())
for i in range(student):
    sex, num = map(int, input().rstrip().split())

    if sex == 1:
        for n in range(num - 1, cnt, num):
            bulb[n] = 1 - bulb[n]

    else:
        num_index = num - 1
        max_size = min(num_index, cnt - num)
        bulb[num_index] = 1 - bulb[num_index]
        for s in range(1, max_size + 1):
            if bulb[num_index - s] == bulb[num_index + s]:
                bulb[num_index - s] = 1 - bulb[num_index - s]
                bulb[num_index + s] = 1 - bulb[num_index + s]
            else:
                break

for j in range(0, cnt, 20):
    print(*bulb[j:j+20])
