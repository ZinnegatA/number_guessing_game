from random import randint

answer = randint(1, 100)
count = 0
variants = ['да', 'д', 'Да', 'Д']
print('Добро пожаловать в числовую угадайку! Давайте начнем игру!')


def is_valid(arg):
    return arg.isdigit() and 1 <= int(arg) <= 100


while True:
    number = input('Введите целое число от 1 до 100: ')
    if is_valid(number):
        number = int(number)
        if number > answer:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            if count in range(10, 51, 10):
                print('У Вас много неправильных попыток, хотите сдаться?')
                if input() in variants:
                    print('Спасибо за игру и удачи в следующий раз!')
                    break
                else:
                    continue
        elif number < answer:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            if count in range(10, 51, 10):
                print('У Вас много неправильных попыток, хотите сдаться?')
                if input() in variants:
                    print('Спасибо за игру и удачи в следующий раз!')
                    break
                else:
                    continue
        elif number == answer:
            count += 1
            print('Вы угадали число с', count, 'попыток! Поздравляем! Хотите сыграть еще раз? (д/н)')
            count = 0
            answer = randint(1, 100)
            if input() in variants:
                print('Спасибо, что играли в мою числовую угадайку! Увидимся в следующем проекте!')
                continue
            else:
                break
    else:
        print('Я принимаю только целые числа от 1 до 100, пожалуйста, повторите попытку')
