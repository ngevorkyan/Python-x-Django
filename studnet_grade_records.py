#Create two more student tuples: student2 and student3 with different data.
student1 = ('Alice Johnson', 12345, 85, 92, 72)
student2 = ('John Johnson', 12346, 70, 60, 80)
student3 = ('Mariam Machabeli', 4566, 90, 90, 90)

# Access and print the name and student ID of each student using indexing.
print(student1[0:2])
print(student2[0:2])
print(student3[0:2])

# Calculate and print the average test score for student1 by accessing the score elements. (Don't use functions, just do the calculation directly)
average1 = sum(student1[2:])/len(student1[2:])
print(average1)

# Create a tuple called all_students that contains all three student tuples (nested tuple).
allstudents = (student1, student2, student3)
print(allstudents)

# Use tuple unpacking to extract the name and ID from student2 into separate variables, then print them.
separate = []

for i in student2[0:2]:
    separate.append(i)
    
print(separate)

# Create a new tuple called student1_updated with the first test score changed to 100 (create a new tuple with the modified value).
mylist = list(student1)
mylist[2] = 100
student1_updated = tuple(mylist)

print(student1_updated)

# Print the total number of students using len() on all_students.
print(len(allstudents))

# Check if student ID 12345 exists in student1 using the in operator.
print(12345 in student1)