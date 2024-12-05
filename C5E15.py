def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

test_scores = []
for i in range(5):
    score = float(input(f"Enter test score {i + 1}: "))
    test_scores.append(score)

average_score = calc_average(test_scores)
print(f"Average test score: {average_score:.1f}")

for score in test_scores:
    grade = determine_grade(score)
    print(f"Test score {score} gets a grade of {grade}")
