rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
          "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

grade = 0
credit = 0
for i in range(20):
    _, a, b = input().split()

    if b == "P":
        continue

    grade += float(a) * rating[b]  # 학점 * 과목평점
    credit += float(a)  # 학점

print(grade / credit)