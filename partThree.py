print("Grade calc")
score = int(input("Please enter a percentage of the grade: "))

if score <= 100 and score >= 90:
    print("This student achieved an A grade")
elif score <= 90 and score >= 80:
    print("This student achieved an B grade")
elif score <= 79 and score >= 70:
    print("This student achieved an C grade")
elif score <= 69 and score >= 60:
    print("This student achieved an D grade")
elif score <= 60:
    print("This student achieved a F")
else:
    print("Enter a percentage score.")
