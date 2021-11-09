def print_field():
    print("         0   1   2")
    for j in range(3):
        print(f"    {j}    {'   '.join(field_out[j * 3:j * 3 + 3])}")
    print()


def check_move(xo_move, c, d):
    if xo_move in field and field[xo_move] not in c.union(d):
        return 0
    else:
        if xo_move not in field:
            print("Нет клетки с такими координатами. Введите корректный ход\n")
        else:
            print("Эта клетка уже занята. Введите другой ход\n")
        return 1


def move_xo(a, c, d):
    global n, field_out
    win_xo = 0
    move = input(f"Введите ход '{a}': ").replace(" ", "")
    print()
    err = check_move(move, c, d)
    if not err:
        c.add(field[move])
        field_out[field[move]] = a
        print_field()

        if n >= 5:
            for win_i in win:
                if len(list(c.intersection(win_i))) == 3:
                    win_xo = 1
                    break
    else:
        n -= 1
    return win_xo


print(""" ----------------------------
   Добро пожаловать в игру
       крестики-нолики
 ----------------------------
  Чтобы сделать ход, введите
   координаты нужной клетки:
    первое число - строка,
    второе число - столбец
  (пробелы не имеют значения)
 ----------------------------""")

win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
field = {'00': 0, '01': 1, '02': 2, '10': 3, '11': 4, '12': 5, '20': 6, '21': 7, '22': 8}

field_x = set()
field_o = set()
field_out = ['.'] * 9
print_field()

n = 1
win_x = 0
win_o = 0
while n < 10 and not win_x and not win_o:
    if n % 2 == 1:
        win_x = move_xo('x', field_x, field_o)
    else:
        win_o = move_xo('o', field_o, field_x)

    n += 1

if n == 10 and not win_x and not win_o:
    print("Ничья")
elif win_x:
    print("Победа х")
elif win_o:
    print("Победа o")