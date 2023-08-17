class Nmy:
    NAMES = ("гражданский военный", "боец из ЧВК")
    NAMES_GUNS = {"гражданский военный": "usps-s", "боец из ЧВК": 'ak-47'}
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Elite_nmy(Nmy):
    def __init__(self):
        super().__init__(Nmy.NAMES[1], 200)

class Simple_nmy(Nmy):
    def __init__(self):
        super().__init__(Nmy.NAMES[0], 100)

class Player:

    def __init__(self, name, gun):
        self.name = name
        self.health = 100
        self.gun = gun

    def __setattr__(self, key, value ):
        if key == "gun" and value not in  Game.GUNS:
            raise AttributeError("Вы не можете выбрать оружия, которого нет в списке")
        if key == "name" and not value:
            raise AttributeError("Поле имя не может быть пустым")
        self.__dict__[key] = value

    
class Game:
    GUNS = ("usps-s", "ak-47", "m4a1-s")
    DAMAGES = {"usps-s": 20, "ak-47": 50, "m4a1-s": 35}

    def __init__(self, p, sim_nmy, el_nmy):
        self.p = p
        self.nmy = sim_nmy
        self.el_nmy = el_nmy

    def __str__(self) -> str:
        return f"name: {p.name}, gun: {p.gun}, health: {p.health}hp, damage: {Game.DAMAGES[p.gun]}hp, nmy_simple: {sim_nmy.name}, el_nmy: {el_nmy.name}"
    
    def start_game(self):
        
        return f"Привет игрок {p.name}, ты играешь в мою текстовую игру на питоне, и похоже ты выбрал пушку {p.gun}, у которой урок {Game.DAMAGES[p.gun]}hp, удачи в бою.\n" 
    
    def frst_nmy(self):
        return f"О нет, это твой первый противник. В самом начале у тебя будут только легкие противники группировки под наименованием {sim_nmy.name}\n Твой hp равен {p.health}\n hp противника равен {sim_nmy.health}"
        
    

if __name__ == "__main__":
    # p = Player(input("Введите ваше имя: "), input(f"Введите оружие из списка {Game.GUNS}: "))
    p = Player("vlad", "ak-47")
    sim_nmy = Simple_nmy()
    el_nmy = Elite_nmy()
    start = Game(Player, sim_nmy, el_nmy)
    print(start)
    print(start.start_game())
    print(start.frst_nmy())
    
    
        
        