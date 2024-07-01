def calculate_gpa(average_grade):
    if average_grade >= 90:
        return 'A', 4.0
    elif average_grade >= 80:
        return 'B', 3.0
    elif average_grade >= 70:
        return 'C', 2.0
    elif average_grade >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

# Function to get input grades from the user
def input_grades(subjects):
    grades = {}
    for subject in subjects:
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade
    return grades

# Function to calculate average grade
def calculate_average_grade(grades):
    total_grade = sum(grades.values())
    return total_grade / len(grades)

# Main program
def main():
    # Define subjects for which grades will be tracked
    subjects = ['Math', 'Science', 'History', 'English']

    # Input grades for each subject
    grades = input_grades(subjects)

    # Calculate average grade
    average_grade = calculate_average_grade(grades)

    # Calculate GPA and letter grade
    letter_grade, gpa = calculate_gpa(average_grade)

    # Display results
    print("\nGrade Report:")
    print("--------------")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"\nAverage Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")

if __name__ == "__main__":
    main()