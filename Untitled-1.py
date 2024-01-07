# def print_recipe(ing_1, ing_2, ing_3, ing_4):
#     print(ing_1 + " " + (ing_3 + " ") * 5 + (ing_4 + " ") * 6 + (ing_2 + " ") * 7 + ing_1)

# print_recipe(input("Введите первый ингредиент: "), input("Введите второй ингредиент: "), input("Введите первый ингредиент: "), input("Введите первый ингредиент: "))

# prod1 = input()
# prod2 = input()
# prod3 = input()
# prod4 = input()
# print(f"{prod1}, {prod2}, {prod3}, {prod4} ")

# team = input()
# print(f"В следующем сезоне {team} выиграет Лигу Чемпионов")

# word = input()
# n = len(word) 
# print("!" + " " * len(word) + "!")

string = "leet"
def palindrom(string: str) -> bool:
    left, right = 0, len(string) - 1
    while string[left] != string[right]:
        if left != right:
            return False
        left += 1
        right -= 1
    return True
print(palindrom(string))




в