def apply_all_func(int_list: list[int, float], *functions: tuple) -> dict:
    results = dict()
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


p1 = apply_all_func([6, 20, 15, 9], max, min)
p2 = (apply_all_func([6, 20, 15, 9], len, sum, sorted))

print(p1)
print(p2)
