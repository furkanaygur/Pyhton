# ************ Tuple ***************
tuple = (1, 'two', 3)
print(tuple[2])
print(type(tuple))
# tuple[0] = 'one'  # 'tuple' object does not support item assignment
example = (1, 'two', 3) + tuple
print(example)
print(type(example))

# ************ Dictionary ***************  key -> value
city = ['istanbul', 'elazığ', 'izmir', 'ankara']  # Cities in Turkey
licensePlate = [34, 23, 35, 6]
print(licensePlate[city.index('ankara')])
licensePlates = {'istanbul': 34, 'ankara': 6}
print(licensePlates['istanbul'])
licensePlates['izmir'] = 35
print(licensePlates)
licensePlates['istanbul'] = 'new value'
print(licensePlates)

##################

users = {
    'furkan': {
        'name': 'furkan',
        'surname': 'aygur',
        'age': 22,
        'roles': 'admin'
    },
    'user2': {
        'name': 'unknown',
        'surname': 'unknown',
        'roles': 'user'
    }
}
print(users['furkan'])
print(users['furkan']['roles'])
if (users['furkan']['roles'] == 'admin'):
    print('he is an admin')
else:
    print('he is not an admin')
###############

students = {}
number = input("Students Number: ")
name = input("Students Name: ")
surname = input("Students Surname: ")
students[number] = {
    'name': name,
    'surname': surname
}
print(students)
#### USE UPDATE
students.update({
    number: {
        'name': name,
        'surname': surname
    }
})
print(students)
