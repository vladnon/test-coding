import random


class Game:
    def __init__(self) -> None:
        self.coins = 10
        self.SIGNS = ('камень', 'ножницы', 'бумага')

# короче я не хочу использовать global, но похоже придется, тк я вроде не могу обернуть это все в класс, потому что мне надо будет передавать self

    def main(self, user, bet):
        enemy = random.choice(self.SIGNS)
        if self.coins < bet:
            return 'Нет коинов', self.coins, enemy
        self.rebalance( user, enemy, bet)
        return self.check(user, enemy), self.coins, enemy, user


    def rebalance(self, user, enemy, bet):
        if self.check(user, enemy) == 'Победа':
            self.coins += bet
        if self.check(user, enemy) == 'Поражение':
            self.coins -= bet
        return self.coins
            

    def check(self, user, enemy):
        if user == enemy:
            return "Ничья"
        if ( 
            user == 'ножницы' and enemy == 'бумага' or
            user == 'камень' and enemy == 'ножницы'or 
            user == 'бумага' and enemy == 'камень'
        ):
            return 'Победа'
        
        if ( 
            enemy == 'ножницы' and  user == 'бумага' or
            enemy == 'камень' and  user == 'ножницы'or 
            enemy == 'бумага' and  user == 'камень'
        ):
            return 'Поражение'

if __name__ == "__main__":
    # print(main('бумага', 10))
    game = Game()
    print(game.main('бумага', 5))