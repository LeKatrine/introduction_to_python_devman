import questions as q

player_score = 0
your_answers = []
true_answers = ["2", "4", "2", "3", "2",
                "1", "3", "1", "3", "3"]

username = input("Как вас зовут?")
print("""Тебе будут заданы 10 вопросов. Каждый вопрос имеет 4 варианта ответа, но только один правильный. Как только ты дашь неправильный ответ, игра закончится. Но есть и приятные бонусы - несгораемые суммы.

После 3 вопроса твой несгораемый выигрыш составит 300 000.
После 7 вопроса он увеличится до 700 000.
Если же ты ответишь на все вопросы правильно, ты получишь 1 000 000!!! Желаю удачи!
""")

for index in range(10):
    print(index)
    print(q.questions_list[index])
    answer = input("Ваш ответ: ")
    your_answers.append(answer)
    if your_answers[index] == true_answers[index]:
        player_score += 1   
    else:
        print(f"Ты неправильно ответил на {index}-й вопрос\n")
        break
    
if player_score < 3:
    print("вы проиграли и ничего не выиграл")
elif player_score >= 3 and player_score < 7:
    print("Вы проиграли, Ваш выигрыш составил 300к")
elif player_score >= 7 and player_score < 10:
    print("Вы проиграли, Ваш выигрыш составил 700к”")
elif player_score == 10:
    print("Вы победили, выигрыш составил 1.000к")


