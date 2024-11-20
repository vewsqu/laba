# TODO решите задачу

import json

def task() -> float:

    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)


    total_sum = 0.0

    for item in data:
        if 'score' in item and 'weight' in item:
            product = item['score'] * item['weight']
            total_sum += product

    return round(total_sum, 3)


result = task()
print(result)
