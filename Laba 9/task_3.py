import os
import string

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



t = TextLoader("/Users/irina/PycharmProjects/pythonProject1/Laba 9/sample")
print(len(t))
print(*t[1])
