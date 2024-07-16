from dataclasses import dataclass
#  когда придешь, тебе надо будет сделать ретерн из каждого метода действия, чтобы потом обновить атрибут класса, тогда игра действительно будет работать, и почти готова


@dataclass
class Option:
    def choose_option(self, player, pot, enemy, bb):
        if player.need_to_call == 0:
            option = input("Choose option: check/fold, raise: \n")
        elif player.need_to_call == player.stack:
            option = input("Choose option: fold, call: \n")
        else:
            option = input("Choose option: fold, call, raise: \n")
        match option:
            case "check":
                return self.check(pot)
            case "fold":
                return self.fold(enemy, pot)
            case "call":
                return self.call(player, pot, enemy)
            case "raise":
                return self.bet(player, pot, enemy, bb)
            case _:
                print("write valid option")
                return self.choose_option(player, pot, enemy, bb)

    def fold(self, enemy, pot):
        return self.give_chips_to_the_winner(enemy, pot), pot


    def bet_preflop(self, bb, pot, player):
        size_bb = {"2": int(bb * 2), "3": int(bb * 3), "4": int(bb * 4), "100": pot}

        size_in_bb = (input(f"Choose bet size: 2bb({size_bb["2"]}), 3bb({size_bb["3"]}), 4bb({size_bb["4"]}), 100%({pot}) of pot or all-in({player.stack}): \n"))
        if size_in_bb not in size_bb:
            print("write valid size")
            size_in_bb = self.bet_preflop(bb, pot, player)
        size = size_bb[size_in_bb]
        return size

    def bet_after_preflop(self, pot, player):
        simple_size = {
            "10": round(pot * 0.1),
            "33": round(pot * 0.33),
            "50": round(pot // 2),
            "75": round(pot * 0.75),
            "100": pot,
            "all-in": player.stack
        }
        size_in_percent = input(f"Choose bet size: 10%({simple_size["10"]}), 33%({simple_size["33"]}), 50%({simple_size["50"]}), 75%({simple_size["75"]}), 100%({pot}) of pot or all-in({player.stack}): \n")
        if size_in_percent not in simple_size:
            print("write valid size")
            size_in_percent = self.bet_preflop(pot, player)
        size = simple_size[size_in_percent]
        return size

    def check_if_player_has_enough_money(self, stack, bet_size):
        if stack > bet_size:
            return True
        else:
            return False

    def choose_size(self, bb, pot, player):
        if pot == bb + (bb // 2):
            size = self.bet_preflop(bb, pot, player)
        else:
            size = self.bet_after_preflop(pot, player)
        if not self.check_if_player_has_enough_money(player.stack, size):
            return size
            self.choose_size(bb, pot, player)
        return size

    def bet(self, player, pot, enemy, bb):
        size = self.choose_size(bb, pot, player)
        player.stack -= size
        player.need_to_call = 0
        enemy.need_to_call += size
        pot += size
        return "raise", pot

    def call(self, player, pot, enemy):
        pot += player.need_to_call
        if player.stack <= player.need_to_call:
            player.stack = 0
            player.need_to_call = 0
        player.stack -= player.need_to_call
        player.need_to_call = 0
        return "call", pot

    def check(self, pot):
        return "check", pot

    def give_chips_to_the_winner(self, player, pot):
        player.stack += pot
        return f"The winner is {player.name}, his prize is {pot} and his stack is {player.stack}"
