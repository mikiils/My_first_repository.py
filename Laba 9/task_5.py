class Off(Exception):
    pass

def connect_user(id):
    file = open(f"/Users/irina/PycharmProjects/pythonProject1/Laba 9/Messages/{id}.txt", "w")
    print("Я создал файл", id)
    yield
    file.close()
    print ("Я закрыл файл", id)
    yield

def write_to_file(id, massage):
    try:
        file = open(f"/Users/irina/PycharmProjects/pythonProject1/Laba 9/Messages/{id}.txt", "x")
        file.write(massage)
        print("Записал")
        file.close()
    except Exception:
        pass

def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"
        write_to_file(username, f"message{i}")

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        ConnectUser = connect_user(id)
        next(ConnectUser)
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"
        next(ConnectUser)
        ConnectUser.close()


def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

#for i in establish_connection(): print(i)
#for i in establish_connection(False): print(i)

for i in connection():
    print(i)


'''disconnect - пользователь ушёл
auth - выполнен вход'''