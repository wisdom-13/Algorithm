import sys
input = sys.stdin.readline

string = input().rstrip()

if '::' in string:
    string = string.replace('::', ':'*(9-string.count(':')))

arr = list(map(lambda x: x.zfill(4), string.split(':')))

print(":".join(arr))