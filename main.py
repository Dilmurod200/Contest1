# main.py
from your_module import kwargsAcceptFun, typeBasedTransformer, decorator_1

# Task 1: Using kwargsAcceptFun
kwargsAcceptFun(name="Dilmurod", age=20, city="Tashkent")

# Task 2: Using typeBasedTransformer
data = {
    "num": 4,
    "text": "hello",
    "flag": True,
    "numbers_list": [1, 2, 3],
    "nested_dict": {"a": 1, "b": 2}
}
transformed_data = typeBasedTransformer(data)
print(transformed_data)

# Task 3: Using decorator_1
@decorator_1
def sample_function():
    time.sleep(2)  # Simulate a delay

sample_function()

