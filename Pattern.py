import re
import os
import numpy as np
from os.path import isfile, join
dir_name = input("Введите имя корневой папки\n") # "D:\Учеба\Programming\Prac_4_sem\root_pattern"
os.chdir(dir_name)
departments = ['analytics', 'R&D', 'marketing', 'accounting', 'engineering'] # названия отделов
for dirname in departments:
    try:
        os.mkdir(dirname) # создание папки для каждого отдела
    except FileExistsError:
        continue
try:
    os.mkdir('Прочее')
except FileExistsError:
    print('Все папки уже созданы!')

letters = list("qwertyuiopasdfghjklzxcvbnm") # спико букв для рандомайзера


def random_files_creation(deps, n):#случайная генерация имен файлов
    global letters
    deps_local = deps.copy() # Копия, иначе не будет отдела прчее
    deps_local.append("a")# файлы из квазинесуществующих отделов
    res = [] # для вывода созданных файлов
    for _ in range(n):# создаем цикл с n итераций
        k = np.random.randint(1, 10, 1) # случайное число букв до и после названия отдела
        filename = ''.join(np.random.choice(letters, k - 1)) + np.random.choice(deps_local) + ''.join(np.random.choice(letters, k)) + ".txt"
        open(filename, "w") # создание файла
        res.append(filename)
    return res


while True:
    print('Еще тест или хватит?')
    deter = input('y or n? \t')
    if deter == 'y':
        n = int(input("Введите количество файлов для создания\n"))
        lst = random_files_creation(departments, n) # получение системой файлов
        print(f"Система получила {n} файлов с именами {lst} ")

        onlyfiles = [f for f in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), f))] # список файлов в корневой папке

        for file_name in onlyfiles: # пробегаем по всем файлам
            re_f = re.findall(r'|'.join(departments), file_name) # ищем паттерн: любое назнвание отдела
            if len(re_f) == 0:# если findall вернула пустой список, то паттерн не найден, следовательно в прочее
                os.replace(file_name, "Прочее" + "/" + file_name) # перемещение
            else:
                os.replace(file_name, re_f[0] + "/" + file_name) # перемещение
    else:
        print('Ok!')
        break
