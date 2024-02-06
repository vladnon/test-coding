import random

class Game:
    SIGNS = ('камень', 'ножницы', 'бумага')
    def __init__(self) -> None:
        self.coin = 10
        
        
        
    def main(self):
        print("\nПривет, в начале у тебя есть 10 коинов\nЕсли ты их поставил и выиграл, то ты их удвоишь\nЕсли же проиграешь, то потеряешь их")
        
        while True or self.coin > 0:
            print(f"\nБаланс: {self.coin}")
            cost = int(input('Сколько ты хочешь поставить коинов: '))
            user = input("\nВведите знак или стоп: ")
            
            if user == 'стоп':
                break
            
            if user not in Game.SIGNS:
                raise AttributeError("Недопустимое значение")
            
            enemy = random.choice(Game.SIGNS)
            
            print(f'Ваш знак: {user}, знак противника {enemy}')
            self.rebalance(user, enemy, cost)
            print(self.check(user, enemy))
        print("Ты проиграл все свои коины, начни игру заново!")
            
            
            
    def rebalance(self, user, enemy, cost):
        if self.check(user, enemy) == 'Пользователь победил':
            self.coin += cost
        if self.check(user, enemy) == 'Компьютер победил':
            self.coin -= cost
        

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
            enemy == 'ножницы' and  user == 'бумага'or 
            enemy == 'ножницы' and  user == 'бумага'
        ):
            return 'Компьютер победил'

if __name__ == '__main__':
    game = Game()
    game.main()