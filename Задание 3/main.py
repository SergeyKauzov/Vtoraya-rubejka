def select1(a, b):
    if not a and not b :
        print('Значения не введены. Повторите Попытку :)')
    else :
        print("Результат =", a * b )


def select2(a, b):
    if not a and not b :
        print('Значения не введены. Повторите попытку :)')
    elif (b == 0):
        print('На ноль делить НЕЛЬЗЯ!')
    else :
        print('Результат = ' , a / b)


def select3():
    return (int(input('Задайте значение A: ')), int(input('Задайте значение B: ')))


userChoice = 0
a, b = False, False

print('Меню:')

print('1. Введите значения A и B')
print('2. Умножить значения A и B')
print('3. Разделить значения A и B')
print('4. Выход')
print('Выберите опцию:')

while userChoice != 4:
        userChoice = int(input())
        if userChoice == 1:
            a,b = select3()
        elif userChoice == 2:
            select1(a,b)
        elif userChoice == 3:
            select2(a,b)
        elif userChoice == 4 :
            print('Был произведен выход из программы. Ещё увидимся :)')
            break
        else:
            print('Ошибка. Такой опции не существует. Повторите попытку :)')

        print('Меню:')
        print('1. Введите значения A и B')
        print('2. Умножить значения A и B')
        print('3. Разделить A на B')
        print('4. Выход')
        print('Выберите опцию:')