
#print("Hello Python from Visual Studio!")
#s = "*"*30
#print(s)
#print("New project")
#print(s)  


import hashlib

dict = {11111: 'Pink', 22222: 'Gray', 33333: 'Petrov', 44444: '553', 55555: 'Anna'}
word = input("Bведите кодовое слово: ")
if word in dict.values():  # Есть ли введенное слово в словаре
    for key, value in dict.items():  # dict.items() - возвращает пары (ключ, значение)
        if value == word:  # Возвращают список всех значений, доступных в данном словаре k
            print("Номер ячейки:", key)
            hash = hashlib.md5(word.encode())  # Возвращает кодированную версию строки
            hash_res = hash.hexdigest()  # Получить зашифрованную последовательность байтов и строку
            print("Хеш кодового слова:", hash_res)
else:
    print("Кодовое слово введено неверно.")