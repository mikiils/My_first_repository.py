class Mother():
    def __str__(self):
        return 'This is print of Mother'

class Daughter(Mother):
    def __str__(self):
        return 'This is print of Daughter'

if __name__ == "__main__":
    print(Mother())
    print(Daughter())