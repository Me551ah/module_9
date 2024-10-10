def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        count = True
        for i in range(2, result):
            if result % i == 0:
                count = False
                break
        print('Простое' if count else 'Составное')
        return result

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c



result = sum_three(2, 3, 6)
print(result)
result = sum_three(7, 4, 9)
print(result)