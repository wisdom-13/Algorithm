n_str = input()
n_arr = n_str.split(' ')

result = int(max(n_arr))*100

for i in n_arr:
    c = n_arr.count(i)
    if c == 1:
        continue
    if c == 2:
        result = 1000+int(i)*100
        break
    if c == 3:
        result = 10000+int(i)*1000
        break

print(result)