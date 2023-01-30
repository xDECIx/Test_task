import os
import pandas as pd


def save_files_to_excel():
    directory = os.path.dirname(os.path.abspath('__main__'))  # Опреляем через модуль свое расположние
    file_list = []
    for root, dirs, files in os.walk(directory): # Проходимся в ней через цикл
        for file in files: # достаем из директории название файла
            path = os.path.join(root, file) # записываем путь в переменную path
            folder, filename = os.path.split(path)
            name = os.path.splitext(filename) # достаем имя
            ext = filename.rsplit('.', 1)[-1] # Расширение начиная с точки слева направо

            file_list.append([folder, name[0], ext]) # записываем в список

    df = pd.DataFrame(file_list, columns=["Папка в которой лежит файл", "Название файла", "Расш.файла"]) # через пандас строим колонны, указываем список
    df['Номер строки'] = range(1, len(df) + 1) # для нумерации
    df.set_index('Номер строки', inplace=True)
    df.to_excel("result.xlsx", index=True) # записываем в эксель

    print("Вы находитесь тут",directory)
    input()
if __name__ == '__main__':
    save_files_to_excel()
