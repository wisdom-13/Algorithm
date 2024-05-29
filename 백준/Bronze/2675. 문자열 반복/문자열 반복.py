s = int(input())

for i in range(s):
    r, s = input().split(' ')
    p = ''
    for i in s:
        p += str(i) * int(r)
    print(p)