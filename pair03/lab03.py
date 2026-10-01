# 1
# text = input('Напишіть текст: ').strip().lower()

# digits = 0
# letters = 0
# vowels = 'aeiouy'
# spaces = 0
# vowels_count = 0
# words = len(text.split())

# for i in text:
#     if i in vowels:
#         vowels_count += 1
#     if i.isdigit():
#         digits += 1
#     if i.isalpha():
#         letters += 1
#     if i == " ":
#         spaces += 1

# print(f'Символів: {len(text)}')
# print(f'Літер: {letters}')
# print(f'Цифр: {digits}')
# print(f'Пробілів: {spaces}')
# print(f'Голосних: {vowels_count}')
# print(f'Слів: {words}')

#2

# text = input('введіть піб')

# parts = text.split()

# if len(parts) == 3:
#     surname = parts[0].capitalize()
#     name = parts[1].capitalize()
#     po_batkyovi = parts[2].capitalize()

#     print(f"{surname} {name[0]}.{po_batkyovi[0]}.")
# else:
#     print("введіть прізвище, ім'я та по-батькові!!!!!!!!!!!!!!!")

#3

# first = input('перший рядок')
# second = input('другий рядок')

# normal1 = first.replace(" ", "").lower()
# normal2 = second.replace(" ", "").lower()

# if sorted(normal1) == sorted(normal2):
#     print("рядки є анаграмами")
# else: 
#     print('не є анаграмами')

#4

# text = input('введіть речення')

# before = input('введіть слово для заміни')
# after = input('слово після заміни')

# words = text.split()
# unique = set(words)
# longest = words[0]
# shortest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

#     if len(word) < len(shortest):
#         shortest = word

# new_text = text.replace(before, after)

# print(f"найдовші:{longest}")
# print(f"найкоротші: {shortest}")
# print(f"унікальних слів: {len(unique)}")
# print(f"після заміни: {new_text}")