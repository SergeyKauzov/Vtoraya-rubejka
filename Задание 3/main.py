def choice1(a, b):
    if not a and not b :
        print('Ошибка!Вы не задали значения. Задайте их')
    else :
        print("Операция выполнена, результат =", a * b )


def choice2(a, b):
    if not a and not b :
        print('Ошибка! Вы не задали значения. Задайте их')
    elif (b == 0):
        print('Ошибка! На ноль делить нельзя')
    else :
        print('Операция выполнена, результат = ' , a / b)


def read():
    return (int(input('Введите значение A: ')), int(input('Введите значение B: ')))


userChoice = 0
a, b = False, False

print('Меню:')
print('1. Введите значения A и B')
print('2. Умножить значения A и B')
print('3. Разделить A на B')
print('4. Выход')
print('Выберите опцию:')

while userChoice != 4:
        userChoice = int(input())
        if userChoice == 1:
            a,b = read()
        elif userChoice == 2:
            choice1(a,b)
        elif userChoice == 3:
            choice2(a,b)
        elif userChoice == 4 :
            print('Вы вышли из программы!До Свидания')
            break
        else:
            print('Ошибка. Выберите существующую опцию')

        print('Меню:')
        print('1. Введите значения A и B')
        print('2. Умножить значения A и B')
        print('3. Разделить A на B')
        print('4. Выход')
        print('Выберите опцию:')