num_list = input().split()

# 1. 받아온 문자열을 문자열 슬라이싱[::-1]을 사용하여 뒤집음
new_num_list = [i[::-1] for i in num_list]

# 2. 뒤집은 문자열이 저장된 리스트중 큰 값을 출력
print(max(new_num_list))
