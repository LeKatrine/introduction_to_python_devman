import math

message = input("Введите сообщение: ")
length = len(message)

first_cipher = message
first_cipher = first_cipher.replace("и", "о")
first_cipher = first_cipher.replace("к", "м")
first_cipher = first_cipher.replace("т", "с")
first_cipher = first_cipher.replace("н", "к")

print("Шифр 1:", first_cipher)

second_cipher = message[::-1]
print("Шифр 2:", second_cipher)

оdd_letters = message[::2]
even_letters = message[1::2]
third_cipher = (оdd_letters 
                + even_letters)
print("Шифр 3:", third_cipher)

first_letter = message[0]
second_letter = message[1]
penultimate_letter = message[-2]
last_letter = message[-1]
fourth_cipher = (last_letter 
                 + penultimate_letter 
                 + message[2:length-2] 
                 + second_letter 
                 + first_letter)
print("Шифр 4:", fourth_cipher)

half_message_length = math.floor(len(message) / 2)
first_part_message = message[:half_message_length]
second_part_message = message[half_message_length:]

fifth_cipher = (second_part_message 
                + first_part_message)
print("Шифр 5:", fifth_cipher)


first_cipher = first_cipher.replace("к", "н")
first_cipher = first_cipher.replace("с", "т")
first_cipher = first_cipher.replace("м", "к")
first_cipher = first_cipher.replace("о", "и")
first_decoding = first_cipher
print("Расшифровка 1:", first_decoding)

second_decoding = second_cipher[::-1]
print("Расшифровка 2:", second_decoding)

half_cipher_length = math.ceil(len(third_cipher) / 2)
оdd_cipher_letters = third_cipher[:half_cipher_length]
even_cipher_letters = third_cipher[half_cipher_length:]

third_decoding = ""
for symbol in range(len(оdd_cipher_letters)):
    third_decoding += оdd_cipher_letters[symbol]
    if symbol < len(even_cipher_letters):
        third_decoding += even_cipher_letters[symbol]
print("Расшифровка 3:", third_decoding)

first_decoded_letter = fourth_cipher[0]
second_decoded_letter = fourth_cipher[1]
penultimate_decoded_letter = fourth_cipher[-2]
last_decoded_letter = fourth_cipher[-1]

fourth_decoding = (last_decoded_letter 
                   + penultimate_decoded_letter 
                   + fourth_cipher[2:length-2] 
                   + second_decoded_letter 
                   + first_decoded_letter)
print("Расшифровка 4:", fourth_decoding)

half_cipher_length = math.ceil(len(fifth_cipher) / 2)
fifth_decoding = (fifth_cipher[half_cipher_length:] 
                  + fifth_cipher[:half_cipher_length])
print("Расшифровка 5:", fifth_decoding)