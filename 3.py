"""Создайте программу для игры в ""Крестики-нолики"".

Пример интерфейса:

   |   | 0
-----------
   |   |
-----------
   | X |
Ввод можно реализовать через введение двух чисел (номеров строки и столбца).
"""

game_field = list(range(1, 10))


def draw_field(field):
    print("-" * 13)
    for i in range(3):
        print("/", field[0+i*3], "/", field[1+i*3], "/", field[2+i*3], "/")
        print("-" * 13)


def take_input(player_token):
    is_0k = False
    while not is_0k:
        print("Выберите ячейку для:", player_token)
        player_answer = int(input())
        if 1 <= player_answer <= 9:
            if str(game_field[player_answer-1]) not in "XO":
                game_field[player_answer-1] = player_token
                is_0k = True
            else:
                print("Эта ячейка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                draw_field(field)
                print(tmp, "выиграл!")
                return
        if counter == 9:
            draw_field(field)
            print("Ничья!")
            return
    draw_field(field)


main(game_field)
