from time import sleep
player_name = input('Сегодня мы сыграем с вами в игру "Кто хочет стать миллионером?". Итак... Как же зовут нашего нового участника?\n')
print(f"{player_name}, добро пожаловать! Начинаем!")

print("""Вот твой первый вопрос:

Кто был первым президентом России?
1. Путин Владимир Владимирович 
2. Ельцин Борис Николавич
3. Медведев Дмитрий Анатольевич
4. Мишустин Михаил Владимирович
""")
first_answer = input("Ваш ответ: ")
if first_answer == "2":
    print("Ответ верный")
    sleep(1)

    print("""
Твой второй вопрос:

Чему в Туле установлен памятник?
1. Хлебу
2. Кексу
3. Бублику
4. Прянику
""")
    
    second_answer = input("Ваш ответ: ")
    if second_answer == "4":
        print("Ответ верный")
        sleep(1)

        print("""
Итак... Твой третий вопрос:

Чего не ела героиня сказки «Гуси-лебеди», когда спасалась с братцем от погони?
1. Пирожок
2. Фуа-гра
3. Кисель
4. Яблоко
""")
        third_answer = input("Ваш ответ: ")
        if third_answer == "2":
            print("Ответ верный")
            sleep(1)

            print("""
И переходим к четвёртому вопросу:

Что обычно едят горячим?
1. Окрошку
2. Гаспачо
3. Рассольник
4. Свекольник
""")
            fourth_answer = input("Ваш ответ: ")
            if fourth_answer == "3":
                print("Ответ верный")
                sleep(1)

                print("""
Вопрос номер пять:
                
Что Китай недавно объявил своим национальным достоянием, вызвав возмущение граждан Южной Кореи?
1. Онигири
2. Кимчи
3. Ушу
4. Группу «BTS»
""")
                fifth_answer = input("Ваш ответ: ")
                if fifth_answer == "2":
                    print("Ответ верный")
                    sleep(1)

                    print("""
Итак... Шестой вопрос сегодняшней игры:
                    
Какой ингредиент знаменитой пиццы «Маргарита» не символизирует ни один из цветов флага Италии?
1. Оливковое масло
2. Томаты
3. Моцарелла
4. Базилик
""")
                    sixth_answer = input("Ваш ответ: ")
                    if sixth_answer == "1":
                        print("Ответ верный")
                        sleep(1)
                    
                        print("""
Твой седьмой вопрос:

В блюде немецкой кухни «Небо и земля» картофель — это земля. А что символизирует небеса?
1. Грибы
2. Петрушка
3. Яблоки
4. Клубника
""")
                            
                        seventh_answer = input("Ваш ответ: ")
                        if seventh_answer == "3":
                            print("Ответ верный")
                            sleep(1)
                    
                            print("""
Продолжаем... Твой восьмой вопрос:

Какое блюдо создал французский повар Андре Дюпон, состоявший на службе у русского графа?
1. Бефстроганов
2. Цыпленок табака
3. Шницель по-венски
4. Ростбиф
""")
                            eighth_answer = input("Ваш ответ: ")
                            if eighth_answer == "1":
                                print("Ответ верный")
                                sleep(1)
                    
                                print("""
И переходим к девятому вопросу:

Неправильное написание какого слова объясняется тем, что мода на блюдо пришла не из Японии, а из Европы?
1. Тэмпура
2. Рамэн
3. Суши
4. Гедза
""")
                                ninth_answer = input("Ваш ответ: ")
                                if ninth_answer == "3":
                                    print("Ответ верный")
                                    sleep(1)
                    
                                    print("""
Финальный, десятый вопрос:
                
Что стало популярным благодаря «Ресторану трех корон», обслуживавшему посетителей Всемирной выставки 1939 года?
1. Коктейли
2. Фастфуд
3. Шведский стол
4. Еда на вынос
""")
                                    tenth_answer = input("Ваш ответ: ")
                                    if tenth_answer == "3":
                                        print("Вы победили, выигрыш составил 1.000к")
                                    else:
                                        print("Вы проиграли, Ваш выигрыш составил 700к")   
                                else:
                                    print("Вы проиграли, Ваш выигрыш составил 700к")
                            else:
                                print("Вы проиграли, Ваш выигрыш составил 700к")
                        else:
                            print("Вы проиграли, Ваш выигрыш составил 300к")   
                    else:
                        print("Вы проиграли, Ваш выигрыш составил 300к")
                else:
                    print("Вы проиграли, Ваш выигрыш составил 300к")   
            else:
                print("Вы проиграли, Ваш выигрыш составил 300к")
        else:
            print("Вы проиграли и ничего не выиграли")
    else:
        print("Вы проиграли и ничего не выиграли")   
else:
    print("Вы проиграли и ничего не выиграли")