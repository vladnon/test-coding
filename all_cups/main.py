def task1(number: str):
    first_3_numbers = ""
    second_3_numbers = ""
    first_2_numbers = ""
    second_2_numbers = ""
    count = 0
    for char in number:
        if char.isdigit():
            count += 1
            if count in [2, 3, 4]:
                first_3_numbers += char
            if count in [5, 6, 7]:
                second_3_numbers += char
            if count in [8, 9]:
                first_2_numbers += char
            if count in [10, 11]:
                second_2_numbers += char

    return f"+7 ({first_3_numbers}) {second_3_numbers}-{first_2_numbers}-{second_2_numbers}"

def task2(n):
    clients = {}

    for _ in range(n):
        user = input()
        client = user.split()[0]
        purchase = round(float(user.split()[1]), 4)
        if client in clients:
            clients[client] += purchase
        else:
            clients[client] = purchase
    for key in clients.keys():
        print(f"{key} {str(clients[key]) + "0"}")

if __name__ == "__main__":
    # number = input()
    # print((task1(number)))
    n = int(input())
    task2(n)
