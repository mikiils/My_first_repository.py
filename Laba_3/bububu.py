import os
import zipfile

massiv = []
file = open("text3.txt", "w")
for current_dir, dirs, files in os.walk("/Users/irina/Downloads/main"):
    for f in files:
        if f.endswith('.py'):
            massiv.append(current_dir)
            break
massiv.sort()
massiv = map(lambda x: x + '\n', massiv)
file.writelines(massiv)
file.close()


file = open("text3.txt", "r")
for line in file:
        print(line.strip())
file.close()