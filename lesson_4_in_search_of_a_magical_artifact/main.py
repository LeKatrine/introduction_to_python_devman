original_text = input("Введите сообщение: ")
print(original_text)
text_length = len(original_text)
print(f"""Количество символов в строке: {text_length}
Второй символ строки: {original_text[1]}
Последний символ строки: {original_text[-1]}
Последние три символа строки: {original_text[-3:]} 
Первые три символа строки: {original_text[:3]}
""")

color_start = 0
color_end = 6
color_name = input("""Выберете цвет текста: 
1.красный
2.синий
3.зелёный
Выбор: """)
if color_name == "1":
    colorized_text = f"\033[31m{original_text[color_start:color_end]}\033[0m"
elif color_name == "2":
    colorized_text = f"\033[34m{original_text[color_start:color_end]}\033[0m"
elif color_name == "3":
    colorized_text = f"\033[32m{original_text[color_start:color_end]}\033[0m" 
else:
    colorized_text = ""
    print("Нет такого варианта")
print(colorized_text)


old_char = input("Введите символ, который хотите заменить: ")
new_char = input("Введите символ, на который хотите заменить: ")
modified_text = original_text.replace(old_char, new_char)
print(f"Текст после замены: {modified_text}")

even_chars = modified_text[1::2]
odd_chars = modified_text[0::2]
reversed_text = original_text[::-1]
print(f"""
Срез по нечётным символам: {odd_chars}
Срез по чётным символам: {even_chars}
Текст с изменённым порядком символов {reversed_text}
""")

middle_index = len(original_text) // 2
swapped_text = f"""Текст с заменой местами левой и правой части: 
{original_text[middle_index:]}{original_text[:middle_index]}"""
print(swapped_text)