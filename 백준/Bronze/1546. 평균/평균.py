n = int(input())

# 1. 입력 점수를 int로 변환하여 list에 저장
score = list(map(int, input().split()))
max_score = max(score)  # 최대 값
total = 0

# 2. 새로운 점수(점수/최대값*100)를 total에 저장
for i in score:
    total += int(i)/int(max_score)*100

# 3. 새로운 점수 총합 / 과목 수
print(total/n)
