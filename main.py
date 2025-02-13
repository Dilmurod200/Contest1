#donebyDilmurod
import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    total_marks = 0
    num_students = random.randint(10, 751)
    for student in range(num_students):
         total_marks += (student ** 2)
    return total_marks 

@decorator_1
def funx(num_students=None):
    print("I am ready to do serious stuff")
    highest_score = float('-inf')

    if num_students is None:
        num_students = random.randint(10, 751)

    scores = [pow(student, 2) for student in range(num_students)]
    for score in scores:
        if score > highest_score:
            highest_score = score
    return highest_score 

if name == "main":
    func()
    funx()
    func()
    funx()
    func()
