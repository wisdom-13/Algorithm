import sys
input = sys.stdin.readline

num = int(input().rstrip())
password_list = [input().rstrip() for _ in range(num)]


# password_list에 문자열을 뒤집은 값이 있는지 체크하여 return
def search_word(text):
    text = text[::-1]
    return text in password_list


# 문자열의 길이와 중앙값을 return
def text_len_median(text):
    return len(text), text[len(text) // 2]


for password in password_list:
    if search_word(password):
        print(*text_len_median(password))
        break