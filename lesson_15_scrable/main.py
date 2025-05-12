import random


LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "Й": 4,
    "К": 2,
    "Л": 2,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 2,
    "Ф": 10,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3
}


def get_random_letter():
    return random.choice(list(LETTER_SCORES.keys()))


def calculate_score(word):
    return sum([LETTER_SCORES.get(char, 0) for char in word.upper()])


def get_word_with_letter(letter):
    while True:
        word = input(f"Введите слово на букву {letter}: ")
        if letter == word[0].upper():
            return word
        print(f"Слово должно начинаться с буквы {letter}. Попробуйте снова")


if __name__ == '__main__':
    player_words = []
    player_scores = []
    random_letter = get_random_letter()

    print(f"Начальная буква: {random_letter}")
    for num in range(2):
        print(f"Игрок {num + 1}")
        player_words.append(get_word_with_letter(random_letter))
        player_scores.append(calculate_score(player_words[num]))

    for num in range(len(player_words)):
        print(f"Игрок {num + 1} ввёл слово {player_words[num]} и набрал {player_scores[num]} очков")
