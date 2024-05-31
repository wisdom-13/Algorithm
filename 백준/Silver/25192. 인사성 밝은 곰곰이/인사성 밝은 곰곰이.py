import sys
input = sys.stdin.readline

num = int(input())

cnt = 0
chat = set()

# 1. 채팅 수 만큼 반복
for i in range(num):
    text = input().rstrip()

    # 2. ENTER가 입력되면 chat에 쌓인 갯수를 cnt에 저장하고 chat을 초기화
    if (text == "ENTER"):
        cnt += len(chat)
        chat = set()
    else:
        chat.add(text)

cnt += len(chat)
print(cnt)
