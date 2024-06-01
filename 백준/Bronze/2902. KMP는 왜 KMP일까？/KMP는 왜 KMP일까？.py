import sys
input = sys.stdin.readline

# 1. -를 기준으로 문자열 자르기
# 2. 각 배열의 첫번째 글자만 가져온 후
# 3. join으로 연결
print("".join(word[0] for word in input().rstrip().split("-")))