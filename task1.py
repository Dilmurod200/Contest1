def kwargsAcceptFun(**data):
    for k, v in data.items():
        print(f"{k}: {v}")
    return data
