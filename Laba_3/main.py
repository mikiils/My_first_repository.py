def write_array(array, file):
    file.writelines(array)
    pass

file = open("text2.txt", "w")
array = ["hello", "world", "!"]
array = map(lambda x: x + '\n', array)
write_array(array,file)
file.close()

file = open("text2.txt", "r")
for line in file:
        print(line.strip())
file.close()