X = int(input())

#  몇 번째 대각선에 있는지 
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1


if diagonal % 2 == 0:
    # 짝수
    numerator = X
    denominator = diagonal - X + 1
else:
    # 홀수
    numerator = diagonal - X + 1
    denominator = X

print(f"{numerator}/{denominator}")