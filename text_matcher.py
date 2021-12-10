from config_util import get_characters_scheme, get_words_scheme

words = get_words_scheme()
characters_scheme = get_characters_scheme()

print("Фильтруемые слова:", words)

# Фраза, которую будем проверять.
phrase = input("Введите фразу для проверки: ").lower().replace(" ", "")


def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    # Keep current and previous row, not entire matrix
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + \
                1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


for key, value in characters_scheme.items():
    # Проходимся по каждой букве в значении словаря. То есть по вот этим спискам ['а', 'a', '@'].
    for letter in value:
        # Проходимся по каждой букве в нашей фразе.
        for phr in phrase:
            # Если буква совпадает с буквой в нашем списке.
            if letter == phr:
                # Заменяем эту букву на ключ словаря.
                phrase = phrase.replace(phr, key)

# Проходимся по всем словам.
for word in words:
    # Разбиваем слово на части, и проходимся по ним.
    for part in range(len(phrase)):
        # Вот сам наш фрагмент.
        fragment = phrase[part: part+len(word)]
        # Если отличие этого фрагмента меньше или равно 25% этого слова, то считаем, что они равны.
        if distance(fragment, word) <= len(word)*0.1:
            # Если они равны, выводим надпись о их нахождении.
            print("Найдено", word, "\nПохоже на", fragment)
