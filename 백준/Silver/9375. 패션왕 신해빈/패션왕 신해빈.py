import sys
input = sys.stdin.readline

def cody(num):
    closet = {}
    for _ in range(num):
        _, type = input().rstrip().split()
        closet[type] = closet.get(type, 0) + 1

    combinations = 1
    for count in closet.values():
        combinations *= (count + 1) 

    return combinations - 1

def main():
    case = int(input().rstrip())

    for _ in range(case):
        num = int(input().rstrip())
        cnt = cody(num)
        print(cnt)

if __name__ == "__main__":
    main()