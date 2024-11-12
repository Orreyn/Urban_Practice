def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        x = list(map(func, [int_list]))
        results[func.__name__] = x[0] # короче без доп допаковки в список оно ругается на int, а без этого 0 выдаёт лишние нафиг ненужные скобки
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))