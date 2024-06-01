import sys
input = sys.stdin.readline

# 1. 0에서 문자열의 길이만큼 10씩 증가하며 반복 
# 2. w 부터 w+10 만큼 자르기 
word = input().rstrip()
print(*[word[w:w+10] for w in range(0, len(word), 10)], sep='\n')
