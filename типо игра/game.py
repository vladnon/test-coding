import random


class Game:
    def __init__(self) -> None:
        self.coins = 10
        self.SIGNS = ('камень', 'ножницы', 'бумага')

# короче я не хочу использовать global, но похоже придется, тк я вроде не могу обернуть это все в класс, потому что мне надо будет передавать self

    def main(self, user, cost):
        if self.coins == 0:
            return '0'
        enemy = random.choice(self.SIGNS)
        self.rebalance( user, enemy, cost)
        return self.check(user, enemy), self.coins, enemy

    def rebalance(self, user, enemy, cost):
        if self.check(user, enemy) == 'Пользователь победил':
            self.coins += cost
        if self.check(user, enemy) == 'Компьютер победил':
            self.coins -= cost
        return self.coins
            

    def check(self, user, enemy):
        if user == enemy:
            return "Ничья"
        if ( 
            user == 'ножницы' and enemy == 'бумага' or
            user == 'камень' and enemy == 'ножницы'or 
            user == 'бумага' and enemy == 'камень'
        ):
            return 'Пользователь победил'
        
        if ( 
            enemy == 'ножницы' and  user == 'бумага' or
            enemy == 'камень' and  user == 'ножницы'or 
            enemy == 'бумага' and  user == 'камень'
        ):
            return 'Компьютер победил'

if __name__ == "__main__":
    # print(main('бумага', 10))
    game = Game()
    print(game.main('бумага', 5))