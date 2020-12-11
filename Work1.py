groupmates = [
{
"name": "Александр",
"surname": "Иванов",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [3, 3, 4]
},
{
"name": "Иван",
"surname": "Петров",
"exams": ["История", "АиГ", "КТП"],
"marks": [4, 4, 4]
},
{
"name": "Кирилл",
"surname": "Смирнов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [5, 5, 5]
}
]
def print_students(students,marks):
    print (u"name".ljust(15), u"surname".ljust(10), u"exams".ljust(30), u"marks".ljust(20))
    for student in students:
        marks1 = student['marks']
        result = (sum(marks1)/len(marks1))
        if result >= need:
            print(student[u"name"].ljust(15),student[u"surname"].ljust(10), str(student[u"exams"]).ljust(30),str(student[u"marks"]).ljust(20))

need = float(input('Введите средний балл :'))
print_students(groupmates,need)
