# 30.01.2023
name_assistant = "Арния"
print(f"Я твой ассистент. Меня зовут {name_assistant}.")
name_user = input("Как мне к тебе обращаться?\n").title()
print(f"\nПриятно познакомиться, {name_user}.")
age_user = int(input("Теперь я знаю, как тебя зовут. А сколько тебе лет?\n"))
print("\nОго, а ты уже взрослый человек. Через 10 лет тебе будет", age_user + 10)
rise_user = float(input("Раз ты такой взрослый человек, то может ты ещё и высокий... Какой у тебя рост?\n"))
rise_assistant = 0.53
print("Да, уж, ты очень высокий, я всего лишь", rise_assistant, "Получается ты выше меня на",
      rise_user - rise_assistant, "м.")
print("\nЯ столько всего о тебе узнала! Я в восторге! Тебя зовут", name_user, ", сейчас тебе", age_user,
      "лет и твой рост", rise_user, "м.\n\n")
print("""Тебе уже не терпится узнать, что я умею? Вот список того, чем я могу помочь:

1. Расскажу, как поднять себе настроение!
2. Расскажу рубаи Омара Хайяма!
3. Дам совет, ведущий к успеху!
""")
answer = input("\nЧто ты выберешь? ")
if answer == "1":
    print("""\nОткройте карту вашего города и вслепую выберите место. Отправляйтесь туда и найдите там что-нибудь интересное.

Я так уже не раз делала - и каждый раз получалось интересное приключение\n""")
elif answer == "2":
    print("""\n"Кто жизнью бит, тот большего добьется.
Пуд соли съевший выше ценит мед.
Кто слезы лил, тот искренней смеется.
Кто умирал, тот знает, что живет!"

Красивые слова. Иногда мне кажется, что это про меня. Сколько сложностей я решила за свою жизнь...\n""")
    sub_answer = input("""Ты первый раз слышишь эти рубаи... 
1. Да?
2. Нет?\n""")
    if sub_answer == "1":
        print("Я рада, что смогла передать тебе древнюю мудрость великого философа")
    elif sub_answer == "2":
        print("Я рада, что какую-то часть своей жизни ты уже несёшь в себе мудрость этих слов")
    else:
        print("""Наверное, это опечатка. У меня есть только варианты 1 или 2.
Давай попробуем в другой раз""")
elif answer == "3":
    print("""\n"Не тот глуп, кто не знает, но тот, кто знать не хочет".
Уверена, что ты и так знаешь эти протые истины. Но на всякий случай...\n""")
else:
    print("""Наверное, это опечатка. У меня есть только варианты 1, 2 и 3.
Давай попробуем в другой раз""")

# Темы:
# 1. Переменные
# - Наименование (кейсы, составные слова, длина, транслит, переводчик)
# - Синтаксис (+PEP8)
# 2. Типы данных
# - str, int, float (+конвертеры)
# - type()
# - сравнение типов
# 3. Функция print()
# - Передача аргументов (конкатенация, перечисление)
# 4. Функция input() 
# 5. УК
