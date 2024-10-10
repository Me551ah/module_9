from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda a, b: a == b, first, second))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything



class MysticBall:
    def __init__(self, *args):
        self.args = args

    def __call__(self):
        return choice(self.args)


print(result)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())