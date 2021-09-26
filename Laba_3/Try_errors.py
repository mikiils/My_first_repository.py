file = open("text.txt", "w")
file.write('type smth\n smth smth\n')
file.close()

F = input()
try:
    with open(F, 'r') as file:
        for line in file:
            print(line.strip())
    file.close()

except FileNotFoundError:
    print("Error! Файл не найден.")
except Exception:
    print("Error!")