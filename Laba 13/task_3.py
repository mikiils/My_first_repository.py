import os
import string
import re

class TextLoader:
    def __init__(self, filename):
        self.filename = filename
        self.files = []
        for current_dir, dirs, files in os.walk(self.filename):
            for k in range(len(files)):
                self.files.append(filename + '/' + files[k])

    def __len__(self):
        return len(self.files)

    def __getitem__(self, n):
        massiv = []
        file = open(self.files[n], "r")
        for line in file:
            massiv.append(line.lower())
            massiv[-1] = massiv[-1].translate(str.maketrans('', '', string.punctuation))
        file.close()
        massiv = map(lambda x: x + '\n', massiv)
        return massiv

    def __getstate__(self):
        # Копируем состояние объекта из self.__dict__, который
        # содержит все атрибуты. Используем dict.copy()
        # во избежании модификации состояния самого объекта.
        state = self.__dict__.copy()
        # Удаляем несериализуемые атрибуты.
        del state['file']
        return state

    def __setstate__(self, state):
        # Восстанавливаем атрибуты объекта.
        self.__dict__.update(state)
        # Восстанавливаем состояние открытого ранее файла. Для этого нам надо
        # заного открыть его и прочитать необходимое количество строк.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Создаем атрибут для file.
        self.file = file

t = TextLoader("/Users/irina/PycharmProjects/pythonProject1/Laba 9/sample")
print(len(t))
print(*t[1])
