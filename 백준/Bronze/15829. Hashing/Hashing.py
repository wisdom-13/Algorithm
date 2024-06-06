import sys
input = sys.stdin.readline


def main():
    L = int(input().rstrip())
    M = 1234567891
    r = 31

    text = input().rstrip()
    result = 0

    for i in range(len(text)):
        num = ord(text[i]) - 96
        result += num * (r ** i)

    print(result % M)


if __name__ == "__main__":
    main()
