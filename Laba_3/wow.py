file = open("text.txt", "w")
file.write('type smth\n smth smth\n')
file.close()

file = open("text.txt", "r")
for line in file:
        print(line.strip())
file.close()