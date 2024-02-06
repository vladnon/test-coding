import random

SIGNS = ('камень', 'ножницы', 'бумага')

coin = 10
        
        
        
# def main(self, user, cost):
#     if user not in Game.SIGNS:
#         raise AttributeError("Недопустимое значение")
    
#     enemy = random.choice(Game.SIGNS)
    
#     self.rebalance(user, enemy, cost)
#     print(self.coin)
#     return self.check(user, enemy)

    
def main(user):
    if user not in SIGNS:
        raise AttributeError("Недопустимое значение")
    
    enemy = random.choice(SIGNS)
    
    return check(user, enemy)

def rebalance(user, enemy, cost):
    if check(user, enemy) == 'Пользователь победил':
        coin += cost
    if check(user, enemy) == 'Компьютер победил':
        coin -= cost
        

def check( user, enemy):
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
        return 'Пользователь проиграл'

if __name__ == "__main__":
    # print(main('бумага', 10))
    print(main('бумага'))