import time

def decorator_1(func):
    def homework(*subjects, **grades):
        start_study = time.time()
        final_score = func(*subjects, **grades)
        end_study = time.time()
        print(f"Execution time of {func.name}: {end_study - start_study} seconds")
        return final_score
    return homework
