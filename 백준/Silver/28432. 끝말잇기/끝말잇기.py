import sys
input = sys.stdin.readline

first_l = ''
last_l = ''
word_arr = []
s_num = int(input().rstrip())

# 1. 입력받은 단어를 word_arr에 저장하고,
#    ?가 입력될 경우 word_arr의 마지막 요소의 마지막 글자를 last_l에 저장함
#    이전 문자가 ?일 경우 입력한 문자의 첫글자를 first_l에 저장함
for i in range(s_num):
    word = input().rstrip()
    if word == "?" and len(word_arr) > 0:
        last_l = word_arr[-1][-1]

    if len(word_arr) > 0 and word_arr[-1] == "?":
        first_l = word[0]

    word_arr.append(word)

a_num = int(input().rstrip())

# 2. 단어의 첫글자가 last_l와 같고, 마지막 글자가 first_l와 같으면서 단어가 word_arr에 없을 경우 출력
for j in range(a_num):
    word = input().rstrip()
    if (((first_l == '' or first_l == word[-1]) and (last_l == '' or last_l == word[0])) and word not in word_arr):
        print(word)
        break
