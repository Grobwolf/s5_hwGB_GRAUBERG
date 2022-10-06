"""Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного
или больше чем имеется в куче.

b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать
29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.
"""
import random
p1 = input()
p2 = input()


def who_take_first(player1, player2):
    is_0k = False
    while not is_0k:
        player1_roll = random.randint(1, 2)
        player2_roll = random.randint(1, 2)
        if player1_roll != player2_roll:
            is_0k = True
    if player1_roll > player2_roll:
        first = player1
        second = player2
        return first, second
    if player1_roll < player2_roll:
        first = player2
        second = player1
        return first, second


def smarty_bot(candy_pool):
    if candy_pool <= 28:
        print("gg ez")
        take = candy_pool
        print(take)
    elif candy_pool == 29:
        print("gg wp")
        take = 1
        print(take)
    else:
        take = random.randint(1, 28)
        if candy_pool < 56:
            take = candy_pool - 29
        print(take)
    return take


def candy_game(player1, player2):
    first, second = who_take_first(player1, player2)
    candy_pool = int(121)
    while candy_pool > 0:
        is_0k = False
        while not is_0k:
            print("Ваша очередь,", first)
            if "bot" in first:
                take = smarty_bot(candy_pool)
            else:
                take = int(input())
            if take <= 28 and take <= candy_pool:
                is_0k = True
                candy_pool -= take
                print("Осталось конфет:", candy_pool)
            if not is_0k:
                print("Ты можешь брать конфеты только в диапазоне от 1 до 28, однако, не больше, чем их осталось")
        if candy_pool > 0:
            is_0k = False
            while not is_0k:
                print("Ваша очередь,", second)
                if "bot" in second:
                    take = smarty_bot(candy_pool)
                else:
                    take = int(input())
                if take <= 28 and take <= candy_pool:
                    is_0k = True
                    candy_pool -= take
                    print("Осталось конфет:", candy_pool)
                if not is_0k:
                    print("Ты можешь брать конфеты только в диапазоне от 1 до 28, однако, не больше, чем их осталось")
            if candy_pool == 0:
                winner = second
                print("Молодец,", winner)
                return
        else:
            winner = first
            print("Молодец,", winner)
            return


candy_game(p1, p2)
