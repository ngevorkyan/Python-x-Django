# Create a set called student1_courses containing the courses a student is enrolled in:
# Add at least 4 course codes (strings)
student1_courses =  {"MATH101", "ENG202", "PHYS150", "HIST110"}

# Create two more sets: student2_courses and student3_courses with different courses (some overlapping courses are okay).
student2_courses = {"MATH101", "ENG202", "SCI450"}
student3_courses = {"MATH101", "ENG202", "BIO220"}

# Print all three sets and observe how the order might differ from how you entered them.
print(student1_courses) 
print(student2_courses)
print(student3_courses)

# Try to add a duplicate course to student1_courses (a course already in the set). Print the set and observe what happens. Write a comment explaining why.
student1_courses = {"MATH101", "ENG202", "MATH101", "ENG202","PHYS150", "HIST110"}
print(student1_courses)

'''
Additional repeated values are removed automatically from the set.
This happens because the set type can handle duplicated values by its nature.
'''

# Remove one course from student2_courses using the remove() method.
student1_courses.remove('HIST110')
print(student1_courses)

# Add a new course to student3_courses using the add() method.
student3_courses.add("SPT010")
print(student3_courses)

# Find and print the courses that both student1_courses and student2_courses have in common (intersection).
print(student1_courses & student2_courses)
print(student1_courses.intersection(student2_courses))

# Find and print all unique courses taken by either student1_courses or student2_courses (union).
print(student1_courses | student2_courses)
print(student1_courses.union(student2_courses))

# Find and print courses that student1_courses has but student2_courses doesn't (difference).
print(student1_courses - student2_courses)
print(student1_courses.difference(student2_courses))

# Check if "MATH101" is in student1_courses using the in operator.
print("MATH101" in student1_courses)

# Create a set of all available courses called all_available_courses with at least 8 courses.
all_available_courses = student1_courses | student2_courses | student3_courses
print(all_available_courses)

# Check if student1_courses is a subset of all_available_courses.
print(all_available_courses.issubset(student1_courses))

# Print the total number of courses in student2_courses using len().
print(len(student2_courses))