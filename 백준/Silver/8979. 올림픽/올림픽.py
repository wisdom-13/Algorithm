n, target = input().split()
targetScore = 0
scoreArr = []

for i in range(int(n)):
    no, g, s, b = input().split()
    score = (int(g) * 10000) + (int(s) * 100) + (int(b) * 1)
    scoreArr.append(score)
    if (no == target):
        targetScore = score

scoreArr.sort(reverse=True)
print(scoreArr.index(targetScore) + 1)