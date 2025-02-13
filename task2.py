def typeBasedTransformer(input_data):
    transformed_output = {}
    
    for key, value in input_data.items():
        if isinstance(value, int) or isinstance(value, float):
            transformed_output[key] = value ** 2
        elif isinstance(value, str):
            transformed_output[key] = value[::-1]
        elif isinstance(value, bool):
            transformed_output[key] = not value
        elif isinstance(value, list) or isinstance(value, tuple):
            transformed_output[key] = value[::-1]
        elif isinstance(value, dict):
            transformed_output[key] = {v: k for k, v in value.items()}

    return transformed_output
