"""
HighestScorerFinder Program

This program takes marks of 5 subjects from the user,
calculates the total marks, finds the highest and lowest scores,
and gives basic performance feedback.
"""

# Inform the user about the input process
print("Please enter your marks of 5 different subjects, but one by one.")

# List to store marks of all subjects
all_marks = []

# Loop to take marks input for 5 subjects
for i in range(1, 6):
    marks = int(input(f"Please enter marks for subject {i} (out of 100): "))
    all_marks.append(marks)

# Display a message before showing results
print("\n......Calculating grade......\n")

# Calculate total marks
total = sum(all_marks)

# Display total, highest, and lowest marks
print(f"Total Mark: {total}")
print(f"Highest Mark: {max(all_marks)}")
print(f"Lowest Mark: {min(all_marks)}")

# Provide performance feedback based on highest mark
if max(all_marks) >= 80:
    print("Excellent performance!")
else:
    print("Needs improvement")
