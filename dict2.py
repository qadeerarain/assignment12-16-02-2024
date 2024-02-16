#create a program that asks the user fr their scores in different subjects and calculates 
#their overall grade based on a grading scale stored in a dictionary.def calculate_overall_grade(subject_scores):
    # Grading scale dictionary
    grading_scale = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }

    # Calculate average score
    average_score = sum(subject_scores.values()) / len(subject_scores)

    # Determine the overall grade based on the grading scale
    for grade, (lower_bound, upper_bound) in grading_scale.items():
        if lower_bound <= average_score <= upper_bound:
            return grade

# Get input for scores in different subjects
subject_scores = {}
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    subject = input(f"Enter the score for subject {i + 1}: ")
    score = float(input("Enter the score for subject {i + 1}: "))
    subject_scores[subject] = score

# Call the function to calculate overall grade
overall_grade = calculate_overall_grade(subject_scores)

# Display the overall grade
print(f"Overall Grade: {overall_grade}")