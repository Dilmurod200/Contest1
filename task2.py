def typeBasedTransformer(data):
    transformed_data = {}
    
    for key, value in data.items():
        if isinstance(value, int) or isinstance(value, float):
            transformed_data[key] = value ** 2  # Square numbers
        elif isinstance(value, str):
            transformed_data[key] = value[::-1]  # Reverse strings
        elif isinstance(value, bool):
            transformed_data[key] = not value  # Invert boolean
        elif isinstance(value, list) or isinstance(value, tuple):
            transformed_data[key] = value[::-1]  # Reverse list/tuple
        elif isinstance(value, dict):
            transformed_data[key] = {v: k for k, v in value.items()}  # Swap keys and values in dict

    return transformed_data
