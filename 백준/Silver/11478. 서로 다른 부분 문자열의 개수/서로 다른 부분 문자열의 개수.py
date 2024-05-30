string = input()
s = []

for i in range(1, len(string) + 1):
    s += [string[j:j+i] for j in range(0, len(string))]

print(len(set(s)))
