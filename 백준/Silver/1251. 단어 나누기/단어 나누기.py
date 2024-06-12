import sys
input = sys.stdin.readline

text = input().rstrip()
text_list = []

# 단어를 세 개의 부분으로 나누는 모든 경우를 고려
for i in range(1, len(text) - 1):
    for j in range(i + 1, len(text)):
        part1 = text[:i]
        part2 = text[i:j]
        part3 = text[j:]
        new_text = part1[::-1] + part2[::-1] + part3[::-1]
        text_list.append(new_text)

# 사전순으로 가장 앞서는 단어 출력
print(min(text_list))
