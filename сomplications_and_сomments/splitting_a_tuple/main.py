t = ((1, 2, 3), (4, 5, 6), 
     (7, 8, 9), (10, 11, 12), 
     (13, 14, 15), (16, 17, 18), 
     (19, 20, 21), (22, 23, 24))

for x, y, z in t:
    a = x
    print(f"Значение X:{x}")
    b = y
    print(f"Значение Y:{y}")
    c = z
    print(f"Значение Z:{z}")
    print(a, b, c)

s = (("я", "б", "л", "о", "к", "о"), ("п", "р", "и", "в", "е", "т"), 
     ("м", "а", "ш", "и", "н", "а"), ("с", "о", "б", "а", "к", "а"))
for one, two, three, four, five, six in s:
    a = one
    b = two
    c = three
    d = four
    e = five
    g = six
    print(a, b, c, d, e, g, sep="")

t = ((1, 1, 1), (4, 5, 6), 
     (2, 2, 2), (10, 11, 12), 
     (3, 3, 3), (16, 17, 18), 
     (4, 4, 4), (22, 23, 24))

for first_number, second_number, third_number in t:
    if first_number == second_number == third_number:
        print("good")
    else:
        print("bad")

import random
has_love = random.randint(0,1)

something = (("Скорость","Сила","Решимость"), ("Гордость", "Радость", "Забота"))
if has_love == 1:
    first_number, second_number, third_number = something[1]
    print(first_number, second_number, third_number)
else:
    first_number, second_number, third_number = something[0]
    print(first_number, second_number, third_number)
    