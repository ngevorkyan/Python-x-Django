students = {
    '1': {'name': 'Alice Johnson',
          'age': 20,
          'Email': 'Alice@school.edu',
          'grades': {'Math': 85, 'Science': 92, 'English': 78}},
    '2': {'name': 'Bob Smith',
          'age': 19,
          'Email': 'Bob@school.edu',
          'grades': {'Math': 78, 'Science': 85, 'English': 88}},
    '3': {'name': 'Carol Davis',
          'age': 21,
          'Email': 'Carol@school.edu',   
          'grades': {'Math': 95, 'Science': 89, 'English': 91}},
}

student_list = [x for x in students]

while True:
    for student in student_list:
        grades_list = list(students[student]["grades"].values())
        if len(grades_list) >= 1:
            average = sum(grades_list) / len(grades_list)
        else:   # FIX: no elif, just else
            print("There are not enough grades")
            average = 0
        students[student].update({"average": average})
        print(f'\nStudent: {students[student]["name"]}')
        print(f'Age: {students[student]["age"]}')
        print(f'Email: {students[student]["Email"]}')
        print(f'Grades: {students[student]["grades"]}')
        print(f'Average: {students[student]["average"]:.2f}')
        print()

    update = input('If you want to update grades press Y else N: ').upper()

    if update == 'Y':
        student = input("Student to edit: ")
        new_subj, new_score = input("Input subject: "), int(input("input score: "))
        students[student]["grades"].update({new_subj: new_score})

    elif update == 'N':
        break

# Top performer
max_score = max([students[s]["average"] for s in student_list])

for student in student_list:
    if students[student]["average"] == max_score:
        print('\nTop performing student:')
        print('------------')
        print(f'{students[student]["name"]} with average grade: {max_score:.2f}')

# Subject Averages Across All Students
print('\nSubject Averages Across All Students: ')
print('------------')

subject_set = set()
for student in student_list:
    subject_set.update(students[student]["grades"].keys())
    
for subject in subject_set:
    total = 0
    count = 0
    for student in student_list:
        if subject in students[student]["grades"]:  # check if this student has it
            total += students[student]["grades"][subject]
            count += 1
    if count > 0:
        average = total / count
        print(f"{subject} : {average:.2f}")

