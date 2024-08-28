ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"

lang = int(input("""Выберите язык: 1.RU // 2.EN """))
message = input("Введите сообщение: ")
message = message.lower()
step = int(input("Введите шаг сдвига: "))
if lang == 1:
    alphabet = ALPHABET_RU
elif lang == 2:
    alphabet = ALPHABET_EN
    
cipher = [alphabet.find(symbol) + step for symbol in message]
print(f"Индексы шифра: {cipher}")
    
ciphertext = "".join([alphabet[index] for index in cipher])
print(f"Шифр: {ciphertext}")

result = "".join([alphabet[index - step] for index in cipher])
print(f"Дешифровка: {result}")


