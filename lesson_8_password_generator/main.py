from string import printable, whitespace
from random import choice

pass_len = 0
status = False
# all_characters = list(printable.replace(whitespace, ""))
all_characters = list(printable.strip())

print("Какой будет длина пароля?")
while pass_len < 7 or pass_len > 20:
    pass_len = int(input("""Приемлемая длина от 7 до 20 символов. 
Введите цифру: """))
    if pass_len < 7:
        print("Слишком короткий. Попробуйте ещё раз")
    elif pass_len > 20:
        print("Слишком длинный. Попробуйте ещё раз")
print("Длина пароля приемлемая. Генерируем новый пароль: ")

while status == False:
    password = "".join(choice(all_characters)
                       for character in range(pass_len))
    print(f"Пароль: {password}")
    answer = input("""Нравится пароль? 1.Да / 2.Нет 
    Ваш ответ: """)
    if answer == "1":
        print("Ваш пароль:", password)
        status = True
    elif answer == "2":
        print("Генерируем новый пароль:")
    else:
        print("Нет такого варианта")
        break
 