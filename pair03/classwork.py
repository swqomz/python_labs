# name = "Sophie"
# city = "Bucha"
# message = "hello world"

# print(len(message)) #повертає к-сть всіх символів

# print(name[0])
# print(name[-1])
# print(message[len(message) - 1])
# print(city[10])

# text = input()

# if len(text) > 0:
#     print(text[0])
# else:
#     print('рядок порожній')

# text = "hello world"
# print(text[:2])
# print(text[2:])
# print(text[2:5])
# print(text[::2]) #через 1 символ
# print(text[::-1]) #розвертає в зворотньому порядку

# text[3] = "3"  #error
# print(text)

# text = "hello world"
# text2 = text.upper()
# print(text2) #caps
# print(text2.lower()) #little
# print(text.capitalize()) #first upper letter(only first word)
# print(text.title()) #every word with upper

# text = "   Python    programming    "
# print(text.lstrip()) #видаляє символи зліва
# print(text.rstrip()) символи справа
# print(text.strip()) з двох боків

# login = 'admin'
# user_login = input("enter your user:")
# if user_login.strip().lower() == login:
#     print("welcome admin!")

# text = "Python"
# for char in text:
#     print(char)

# password = '123qwerty123'
# # print(password.isdigit())
# digits = 0

# for i in password:
#     if i.isdigit():  #перевіряє чи строка складається з цифр
#         digits += 1 
#     if i.isalpha():
#         letters += 1
# print(f'цифр: {digits}, літер: {letters}') 

# print(password.isalpha()) #перевіряє чи з тільки літерами
# print(password.isdigit) #перевіряє чи з тільки цифрами
# print(password.isalnum) #перевірка тільки на літери\цифри, без символів(пробіл, коми тд)

# text = input('type sentence').strip().lower()
# golosni = 'аеиіїуюоя'

# counter_golosni = 0

# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print(counter_golosni) 

# text = 'привіт      світ'
# words = text.split()
# print(words)

# text_new = ' '.join(words) #обернене до спліта, додає 
# print(text_new)

# text = "Python is easy to learn"
# new_text = text.replace('Python', 'JavaScript')
# print(new_text)

# word = 'Дід '
# word_norm = word.strip().lower()
# if word_norm == word_norm[::-1]:
#     print('паліндром')
# else:
#     print('ne')

# text = 'hello world'

# print(text.find('o')) #положення букви, виводить першу знайдену
# print(text.count('l')) #к-сть 

# email = 'swqomz@gmail.com'
# if email.lower().endswith('@gmail.com'): #.starstwith() початок
#     print('you have google email')