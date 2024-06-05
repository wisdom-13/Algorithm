import math
import sys
input = sys.stdin.readline

# 알파벳 -> 숫자 : 대소문자를 변경 > 아스키코드 변환 > -64
def strToInt(str):
    num = 38 if str.isupper() else 96
    return (ord(str) - num)


# 소수 판별 : 2부터 x의 제곱근까지의 숫자만 확인하면 됨
def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


textArr = (list(map(lambda x: strToInt(x), list(input().rstrip()))))

print("It is a prime word." if primenumber(
    sum(textArr)) else "It is not a prime word.")
