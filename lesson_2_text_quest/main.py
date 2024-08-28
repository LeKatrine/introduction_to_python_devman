player_name = input("Привет тебе, Странник, как тебя зовут? ")
print("""Приятно знать твоё имя! 
Самое время отправляться в путешествие!\n""")

player_score = 0
has_first_artefact = False
has_second_artefact = False
has_third_artefact = False

print(f"""{player_name}, ты начинаешь игру с {player_score} очков. 
Они даются за правильные ответы:
за 1-е задание - 10 очков
за 2-е задание - 20 очков
за 3-е задание - 30 очков

Когда пройдёшь все задания, за очки ты сможешь купить интересные вещи в нашем волшебном магазинчике.
Ещё, за каждое успешное задание ты получишь уникальный артефакт, который поможет тебе  победить в игре.
\n""")

first_answer = input("""Первый вопрос нашего квеста:
Два медвежонка нашли головку сыра. Они долго спорили, как ее поделить, но никто не хотел уступать. 
Мимо пробегала лиса. Узнав, о чем спор, она предложила помочь, разломив головку сыра на 2 части так, 
чтобы одна из них была полкилограмма, а другая меньше. Затем она спросила, усмехаясь: 
- Куски равны?
Жадные медвежата дали отрицательный ответ. Тогда лиса откусила от большей части, но так, чтобы от нее 
остался кусок меньше, чем другая часть, и повторила вопрос. И на этот раз медвежата сообщили, что получились 
неравные части. После этого лиса повторила откусывание еще 9 раз, каждый раз откусывая одинаковое количество 
сыра. В результате остались маленькие кусочки, причем один из них оказался на 20 граммов больше другого. 
Лиса заявила, что медвежатам трудно угодить. Она отправила оба кусочка в рот и, вильнув хвостом, скрылась 
в кустах. Какова была масса головки сыра в граммах?

Введите ответ (цифрами): \
""")
if first_answer == "980":
    first_answer_points = 10
    player_score = player_score + first_answer_points
    has_first_artefact = True
    print("""Не знаю, отгадал ты или действительно посчитал, но ты прав! 
    У тебя теперь {0} очков
    Так же ты нашёл первый артефакт: "Звериный голод", который обуял медвежат, когда лиса их обманула\n""".format(player_score))
else:
    player_score = 0
    print("""Эх... Всё таки ответ не такой. К сожалению, ты не нашёл артефакта.
    Сейчас у тебя {0} очков\n""".format(player_score))

second_answer = input("""Второй вопрос нашего квеста:
Что настолько невероятно хрупкое, что простое произнесение его имени разрушит его?
Введите ответ (текстом, с большой буквы): \
""")
if second_answer == "Тишина":
    second_answer_points = 20
    player_score = player_score + second_answer_points
    has_second_artefact = True
    print("""Да, это она! 
    У тебя теперь {0} очков,
    и артефакт "Звучание тишины", который теперь звенит в твоей голове. Жаль только, что это звучание нарушается урчанием "Звериного голода"\n""".format(player_score))
else:
    player_score = player_score + 0
    print("""Жаль. Это неверный ответ.. Второго артефакта нигде нет - пойдём без него.
    Пока у тебя остаётся {0} очков\n""".format(player_score))

third_answer = input("""Третий вопрос нашего квеста:
Что не умеет разговаривать, однако каждый раз отвечает, когда к нему обращаются?
Введите ответ (текстом, с большой буквы): \
""")
if third_answer == "Эхо":
    third_answer_points = 30
    player_score = player_score + third_answer_points
    has_third_artefact = True
    print("""Да, это эхо! Оно ответило тебе и дало новый артефакт - "Вибрации рекурсии"
    У тебя теперь {0} очков\n""".format(player_score))
else:
    player_score = player_score + 0
    print("""Жаль. Не вышло. И артефакта здесь никакого нет... Даже самого малюсенького.
    У тебя всё ещё {0} очков\n""".format(player_score))

apple = False
apple_cost = 13

tangle = False
tangle_cost = 27

icecream = False
icecream_cost = 14

magic_carpet = False
magic_carpet_cost = 30

print("""Ты завершил испытание! Теперь можешь проследовать в магазин и выбрать себе что-нибудь одно:
1. молодильное яблоко""", apple_cost, """очков
2. волшебный клубок""", tangle_cost, """очков
3. мороженое""", icecream_cost, """очков
4. ковер-самолёт""", magic_carpet_cost, """очков
5. пропустить
""")

while True:
    product = input("Прошу, выбирай то, что тебе по карману: ")
    
    if product == "1" and player_score >= apple_cost:
        apple = True
        player_score = player_score - apple_cost
        print("Теперь у тебя есть яблоко!")
        break    
    elif product == "1" and player_score < apple_cost:
        print(f"Яблоко стоит {apple_cost} очков, а у тебя их всего {player_score}. Выбери что-то другое.")
            
    elif product == "2" and player_score >= tangle_cost:
        tangle = True
        player_score = player_score - tangle_cost
        print("Теперь у тебя есть клубок!")
        break
    elif product == "2" and player_score < tangle_cost:
        print(f"Клубок стоит {tangle_cost} очков, а у тебя их всего {player_score}. Выбери что-то другое.")
    
    elif product == "3" and player_score >= icecream_cost:
        icecream = True
        player_score = player_score - icecream_cost
        print("Теперь у тебя есть мороженное!")
        break
    elif product == "3" and player_score < icecream_cost:
        print(f"Мороженное стоит {icecream_cost} очков, а у тебя их всего {player_score}. Выбери что-то другое.")
    
    elif product == "4" and player_score >= magic_carpet_cost:
        magic_carpet = True
        player_score = player_score - magic_carpet_cost
        print("Теперь у тебя есть ковёр!")
        break
    elif product == "4" and player_score < magic_carpet_cost:
        print(f"Ковёр стоит {magic_carpet_cost} очков, а у тебя их всего {player_score}. Выбери что-то другое.")
    
    elif product == "5":
        print("Хорошо, тогда продолжим без покупок")
        break
    
    else:
         print("Не понял твоего ответа. Покупаем что-нибудь или нет? Набери цифру от 1 до 5 и мы продолжим")



if has_first_artefact and has_second_artefact and has_third_artefact:
    print(f"Поздравляем, ты собрал все артефакты и ты победил! Твой счёт: {player_score} очков!")

elif has_first_artefact == True and has_second_artefact == True and has_third_artefact == False:
    print(f"К сожалению, ты не нашёл третий артефакт! Твой счёт: {player_score} очков!")

elif has_first_artefact == True and has_second_artefact == False and has_third_artefact == True:
    print(f"К сожалению, ты не нашёл второй артефакт! Твой счёт: {player_score} очков!")

elif has_first_artefact == False and has_second_artefact == True and has_third_artefact == True:
    print(f"К сожалению, ты не нашёл первый артефакт! Твой счёт: {player_score} очков!")

elif has_first_artefact == True or has_second_artefact == True or has_third_artefact == True:
    print(f"К сожалению, ты нашёл только один артефакт! Твой счёт: {player_score} очков!")

else:
    print(f"К сожалению, ни один артефакт не собран! Твой счёт: {player_score} очков!")
    

    