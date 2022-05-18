from testsystem import test

def task1(x):
    return 2 * x

def task2(x, y):
    return x + y

print("Проверка задачи 1")
print(task1(10))  # должно быть 20
print(task1(5))  # должно быть 10
print(task1(42))  # должно быть 84

test(task1, "task_example.json")  

print("Проверка задачи 2")
print(task2(10, 20))  # должно быть 30
print(task2(0, 5))  # должно быть 5
print(task2(42, 123))  # должно быть 165

test(task2, "task_example_2.json")  
