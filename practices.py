numbers = [1, 2, 3, 4, 5, 6, 1, 3, 2, 4, 1, 10]
numbers.append(11)
numbers.remove(5)
print(numbers)
print(numbers[4])
global_list = [[1, 2, 3, 4], ["Donald", "Gabriel", "Savior", "Christiana"], [True, False], [10.3, 2.4, 3.5]]
print(global_list)
print(global_list[1])

# Tuple
python_students = ("Angel", "Gabriel", "Daniel")
print(python_students)
print(python_students.append("Saviour"))
python_students['Angel'] = "Daniel"
print(python_students)
x, y, w = python_students
print(x, y, w)

# sets
numbers_set = {3, 2, 1, 5, 2, 2, 6, 5, 1, 10}
print(numbers_set)
numbers_set[10] = 44
print(numbers_set)

# dict
class_dictionary = {
    "name": "Gabriel",
    "score": 22.3,
    "age": 77,
    "is_married": False,
    
}
class_dictionary["name"] = "Daniel"
class_dictionary["course"] = "Python"
del class_dictionary["age"]
print(class_dictionary)