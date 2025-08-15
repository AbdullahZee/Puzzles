class student():
    def __init__(self, name, age, id,):
        self.name = name
        self.age = age
        self.id = id

students = {
    'student1' : {
        'name' : 'Albert',
        'age' : 16,
        'ID' : 1234567890
    },
    'student2' : {
        'name' : 'Sam',
        'age' : 15,
        'ID' : 1234567890
    },
    'student3' : {
        'name' : 'Robert',
        'age' : 17,
        'ID' : 1234567890
    }
}

for y in students.values():
    student(y['name'],y['age'],y['ID'])
