import sys
input = sys.stdin.readline


# 패스워드 리스트를 받아서, 뒤집은 패스워드가 존재하는지 여부를 체크하고 길이와 중앙값을 return
def search_reversed_password(passwords):
    for password in passwords:
        if password[::-1] in passwords:
            return len(password), password[len(password) // 2]
    return None


def main():
    num = int(input().rstrip())
    password_list = set(input().rstrip() for _ in range(num))
    result = search_reversed_password(password_list)

    if result:
        print(*result)


if __name__ == "__main__":
    main()
