import sys
input = sys.stdin.readline

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input().rstrip()
for i in arr:
    text = text.replace(i, "@")

print(len(text))