from dataclasses import dataclass


@dataclass
class Action:
    def choose_action(self, player, pot, enemy):
        if player.need_to_call == 0:
            action = input("Choose action: check/fold, raise: \n")
        else:
            action = input("Chooes action: fold, call, raise: \n")
        match action:
            case "check":
                return self.check()
            case "fold":
                return self.fold(enemy, pot)
            case "call":
                return self.call(player, pot)
            case "raise":
                return self.bet(player, pot, enemy)

    def fold(self, enemy, pot):
        return self.give_chips_to_the_winner(enemy, pot)

    # u need to add bets if its preflop, and u dont have pot, just 2bb, 3bb   
    def bet(self, player, pot, enemy):
        simple_size = {10: pot // 100 * 10,
                33: pot // 100 * 33,
                50: pot // 2,
                75: pot // 100 * 75,
                100: pot 
            }
        size_in_percent = int(input(f"Choose bet size: 10%({simple_size[10]}), 33%({simple_size[33]}), 50%({simple_size[50]}), 75%({simple_size[75]}), 100%({pot}) of pot: \n"))
            
        size = simple_size[size_in_percent]
        
        if player.stack >= simple_size[size_in_percent]:
            if player.stack == size:
                print("all in")
            player.stack -= size
            enemy.need_to_call += size
            pot += size
        else:
            print("u dont have enough money")
            return self.bet(player, pot, enemy)

        return "raise"

    def call(self, player, pot):
        pot += player.need_to_call
        print(player.need_to_call)
        player.stack -= player.need_to_call
        player.need_to_call = 0
        return "call"

    def check(self):
        return "check"

    def give_chips_to_the_winner(self, player, pot):
        player.stack += pot
        return f"The winner is {player.name}, his prize is {pot} and his stack is {player.stack}"
