pole = ['-', '-', '-', 
        '-', '-', '-',
        '-', '-', '-']

vuigrushi = [(0, 1, 2),
             (3, 4, 5),
             (6, 7, 8),
             (0, 3, 6),
             (1, 4, 7),
             (2, 5, 8),
             (0, 4, 8),
             (2, 4, 6)]

pokazateli = {(0, 0): 0,
              (0, 1): 1,
              (0, 2): 2,
              (1, 0): 3,
              (1, 1): 4,
              (1, 2): 5,
              (2, 0): 6,
              (2, 1): 7,
              (2, 2): 8}



#Проверка выигрыша
def vuigrush(pol):
    for vuigr in vuigrushi:
        if pol[vuigr[0]] == pol[vuigr[1]] == pol[vuigr[2]] == 'x':
            return 'X'
        if pol[vuigr[0]] == pol[vuigr[1]] == pol[vuigr[2]] == 'o':
            return 'O'
    return False


#Проверка правильности координат
def proverka_pravilnosti_koordinat(*cifru):
    if (0 <= cifru[0] <= 2) and  (0 <= cifru[1] <= 2):
        return True
    else:
        return False

#Отображение поля
def pole_vision(pol):
    print(f'  0 1 2')
    k = 0
    p = 0
    for i in range(len(pol)):
        if k == 0:
            print(p, end=' ')
            p += 1
        print(pol[i], end=' ')
        k += 1
        if k == 3:
            print()
            k = 0
    print()
    pass


#Сама игра
def game(symbol):
    while True:
        pole_vision(pole)
        print(f'Ход игрока - {symbol}')

        try:
            stroka = int(input("Введите строку (0-2): "))
            stolbec = int(input("Введите столбец (0-2): "))
        except ValueError:
            print("Некорректный ввод! Введите числа от 0 до 2.")
            continue

        if not proverka_pravilnosti_koordinat(stroka, stolbec):
            print("Координаты вне диапазона! Попробуйте снова.")
            continue

        index = pokazateli[(stroka, stolbec)]

        #Проверка на занятость клетки
        if pole[index] != '-':
            print("Эта клетка уже занята! Выберите другую.")
            continue


        pole[index] = symbol

        winner = vuigrush(pole)
        if winner:
            pole_vision(pole)
            print(f'УРА! Победил игрок {winner}')
            break

        #Проверка на ничью
        if not '-' in pole:
            pole_vision(pole)
            print('НИЧЬЯ!')
            break

        #Смена игрока
        if symbol == 'x':
            symbol = 'o'
        else:
            symbol = 'x'


first_symb = input("Кто первый? Х или О: ").lower()
while first_symb not in ['x', 'o']:
    print("Некорректный ввод! Введите Х или О.")
    first_symb = input("Кто первый? Х или О: ").lower()


game(symbol=first_symb)

