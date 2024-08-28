import random


count = 0
for attemp in range(10):
    player = int(input("Сделайте ход: 1-камень, 2-ножницы, 3-бумага, 4-ящерица, 5-спок: "))
    if player == 1:
        print("Ваш ход - камень")
    elif player == 2:
        print("Ваш ход - ножницы")
    elif player == 3:
        print("Ваш ход - бумага")
    elif player == 4:
        print("Ваш ход - ящерица")
    elif player == 5:
        print("Ваш ход - спок")
    else:
        print("Нету токого варианта ответа")
    
    comp = random.randint(1, 5)
    if comp == 1:
        print("Ход компьютера - камень")
    elif comp == 2:
        print("Ход компьютера - ножницы")
    elif comp == 3:
        print("Ход компьютера - бумага")
    elif comp == 4:
        print("Ход компьютера - ящерица")
    elif comp == 5:
        print("Ход компьютера - спок")
        
    if player == comp:
        print("""Ничья!\n
        Победы: """, count,"\n")
    elif player == 1 and (comp == 2 or comp == 4) or \
         player == 2 and (comp == 3 or comp == 4) or \
         player == 3 and (comp == 1 or comp == 5) or \
         player == 4 and (comp == 3 or comp == 5) or \
         player == 5 and (comp == 1 or comp == 2):
         count += 1
         print("""Игрок победил!\n
         Победы: """, count,"\n")
    else:
        print("""Компьютер победил!\n
        Победы: """, count,"\n")
    if count == 3:
        break
print("-" * 46, """\nСТАТИСТИКА ЗА ВСЮ ИГРУ
Победы:""", count)
    

