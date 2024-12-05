def gradeExam(studentAnswers, correctAnswers):
    numCorrect = sum([1 for s, c in zip(studentAnswers, correctAnswers) if s == c])
    numIncorrect = len(studentAnswers) - numCorrect
    passed = numCorrect >= 15

    print("Passed:" if passed else "Failed:")
    print("Number of correctly answered questions:", numCorrect)
    print("Number of incorrectly answered questions:", numIncorrect)
    if numIncorrect > 0:
        print("Incorrectly answered question numbers:", [i+1 for i, (s, c) in enumerate(zip(studentAnswers, correctAnswers)) if s != c])


correctAnswers = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
studentAnswers = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
gradeExam(studentAnswers, correctAnswers)
