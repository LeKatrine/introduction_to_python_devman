win = False
all_letters = []
true_letters = []
points = [0, 0, 0]
counter = 0

secret_word = input("Введите слово для игры: ").lower().strip()
print("\033[2J", "\u001b[1A", end="")

while win == False:
    letter = input(f"\nИгрок {counter+1}, введите букву: ")
    print("Все использованные буквы: ", "".join(all_letters))
    
    if letter in all_letters:
        print("Такая буква уже была")
    elif letter in secret_word:
        true_letters.append(letter)
        points[counter] += 1
        print(f"Это правильная буква! Ваши очки: {points[counter]}")        
    else:
        print("Нет такой буквы в слове")
        counter += 1
        if counter > 2:
            counter = 0
        
    all_letters.append(letter)
    print("\nСлово: ", end="")
    win = True  
    for symbol in secret_word:
        if symbol in true_letters:
            print(symbol, end="")
        else:
            print("*", end="")
            win = False
    
print(f"""\nВы победили!
Игрок 1: {points[0]}
Игрок 2: {points[1]}
Игрок 3: {points[2]}
""")






