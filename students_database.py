
def students_database():
    students = []
    student_id = 1

    while True:
        name = input("enter your name here (or stop to view all students): ").lower().strip()

        if (name == 'stop'):
            break

        for student in students:
            if (name == student[1]):
                print("This name is already present. Plz try another name")

        else : 
            students.append((student_id,name))
            student_id += 1

    print()

    print(f"List of all students: {students}") 

    print()
    print("All students with their ID's and Name's")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")  

    # total no. of students
    print(f"Total students : {len(students)}")   


    # lambda fn kisi bhi list se kisi ak element to return(select) krwany k liye use hota ha, is liye yahann use kia ha (multi inputs --> single output)

    if students:
        longest_name_student = max(students, key=lambda student: len(student[1])) # 
        shortest_name_student = min(students, key=lambda student: len(student[1]))

        print(f"Longest name: {longest_name_student[1]}") 
        print(f"Shortest name: {shortest_name_student[1]}")                 

    # total length of all names

    total_length = 0
    for student in students:
        total_length += len(student[1])

    print(f"Total length of all students' names: {total_length}")

students_database()