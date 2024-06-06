from heapq import *
import sys
input = sys.stdin.readline


def digit_calculation(alphabet, digit):
    number = ord(alphabet) - 96
    return number * (31**digit)


def main():
    int(input().rstrip())
    string_list = list(input().rstrip())
    result = 0

    for entry in enumerate(string_list):
        index, value = entry
        result += digit_calculation(value, index)

    print(result)


if __name__ == "__main__":
    main()
