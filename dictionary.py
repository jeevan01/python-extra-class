student1 = {'rollnum': 1, 'age': 21, 'height': 5.7, 'name': 'Ankit'}
student2 = {'rollnum': 2, 'age': 19, 'height': 5.2, 'name': 'Asmita Neupane'}
student3 = {'rollnum': 3, 'age': 20, 'height': 5.1, 'name': 'Ashmita Subedi'}
students_list = [student1, student2, student3]
# print(students_list)
# print(len(students_list))

for student in students_list:
    print("Roll :\t"+str(student["rollnum"]))
    print("Name :\t"+student["name"])
    print("Age :\t"+str(student["age"]))
    print("height:\t"+str(student["height"]))
    print("\n")
    print("------------------")