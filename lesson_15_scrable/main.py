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
    converted_dictionary = list(LETTER_SCORES.keys())
    random_letter = random.choice(converted_dictionary)
    return random_letter
    # return random.choice(list(LETTER_SCORES.keys()))


def get_word_with_letter(letter):
    while True:
        word = input(f"Введите слово на букву {letter}: ").upper()
        if letter == word[0]:
            return word
        else:
            print(f"Слово должно начинаться с буквы {letter}. Попробуйте снова")



def calculate_score(word):
    all_scores = []
    for char in word:
        scores = LETTER_SCORES.get(char, 0)
        all_scores.append(scores)
        print(char, scores)
    sum_scores = sum(all_scores)
    print(sum_scores, all_scores)




if __name__ == '__main__':
    calculate_score(get_word_with_letter(get_random_letter()))
    calculate_score("Привет")