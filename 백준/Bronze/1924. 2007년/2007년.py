m, d = input().split(' ')
dayArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월별 마지막 일자
weekArr = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 해당 날짜가 1월 1일로부터 몇번째 날인지 계산
day = int(d)
for i in range(int(m) - 1):
    day += dayArr[i]

print(weekArr[day % 7])
