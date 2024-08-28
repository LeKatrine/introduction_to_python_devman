import random

counter = 0
rounds_number = 10

for round in range(rounds_number):
    print(f"{round+1}-й раунд")
    
    player = int(input("Сделайте ход - 1-камень, 2-ножницы, 3-бумага: "))
    if player == 1:
        print("Ваш ход - камень")
    elif player == 2:
        print("Ваш ход - ножницы")
    elif player == 3:
        print("Ваш ход - бумага")
    else:
        print("Возможно ввести только цифры 1, 2, или 3")
    
    comp = random.randint(1, 3)
    if comp == 1:
        print("Ход компьютера - камень")
    elif comp == 2:
        print("Ход компьютера - ножницы")
    elif comp == 3:
        print("Ход компьютера - бумага")

    if player == comp:
        print("Ничья!")
    elif player == 1 and comp == 2 or 
         player == 2 and comp == 3 or 
         player == 3 and comp == 1:
        print("Вы победили!")
        counter += 1
    else:
        print("Вы проиграли!")
    print("Мои победы: ", counter, "\n")

    if counter == 3:
        break