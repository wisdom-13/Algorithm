n = int(input())
line = int(n*2-1)

for i in range(line):
    v = i + 1
    if i < n:
        print('*' * v + ' ' * ((n-v)*2) + '*' * v)
    else:
        print('*' * (line - i) + ' ' * ((v-n)*2) + '*' * (line - i))