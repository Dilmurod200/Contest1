# main.py
from your_module import kwargsAcceptFun, typeBasedTransformer, decorator_1

kwargsAcceptFun(name="Dilmurod", age=20, city="Tashkent")

data = {
    "num": 9,
    "text": "python",
    "flag": True,
    "items": [7, 8, 9],
    "dict_data": {"alpha": 1, "beta": 2}
}
result = typeBasedTransformer(data)
print(result)

@decorator_1
def demo_function():
    time.sleep(2)

demo_function()
