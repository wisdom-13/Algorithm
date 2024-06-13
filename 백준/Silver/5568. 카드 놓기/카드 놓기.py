from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
card_list = []
text_list = set()

for _ in range(N):
    card_list.append(int(input().rstrip()))

# 순열 리스트를 각각 문자열 합치기 
for card in set(permutations(card_list, K)):
    text_list.add("".join(map(str, card)))

print(len(text_list))