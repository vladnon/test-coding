from dataclasses import dataclass
#  когда придешь, тебе надо будет сделать ретерн из каждого метода действия, чтобы потом обновить атрибут класса, тогда игра действительно будет работать, и почти готова


@dataclass
class Action:
    def choose_action(self, player, pot, enemy, bb):
        if player.need_to_call == 0:
            action = input("Choose action: check/fold, raise: \n")
        else:
            action = input("Chooes action: fold, call, raise: \n")
        match action:
            case "check":
                return self.check(pot)
            case "fold":
                return self.fold(enemy, pot)
            case "call":
                return self.call(player, pot)
            case "raise":
                return self.bet(player, pot, enemy, bb)
            case _:
                return self.choose_action(player, pot, enemy, bb)

    def fold(self, enemy, pot):
        return self.give_chips_to_the_winner(enemy, pot), pot

    def all_in(self, player, pot):
        pass

    def bet_preflop(self, bb, pot):
        size_bb = {2: bb * 2, 3: bb * 3, 4: bb * 4, 100: pot}

        size_in_bb = int(
            input(
                f"Choose bet size: 2bb({size_bb[2]}), 3bb({size_bb[3]}), 4bb({size_bb[4]}), 100%({pot}) of pot: \n"
            )
        )
        size = size_bb[size_in_bb]
        return size

    def bet_after_preflop(self, pot):
        simple_size = {
            10: int(pot // 100 * 10),
            33: int(pot // 100 * 33),
            50: int(pot // 2),
            75: int(pot // 100 * 75),
            100: pot,
        }
        size_in_percent = int(
            input(
                f"Choose bet size: 10%({simple_size[10]}), 33%({simple_size[33]}), 50%({simple_size[50]}), 75%({simple_size[75]}), 100%({pot}) of pot: \n"
            )
        )
        size = simple_size[size_in_percent]
        return size

    def check_if_player_has_enough_money(self, stack, bet_size):
        if stack >= bet_size:
            return True
        else:
            return False

    def choose_size(self, bb, pot, stack):
        if pot == bb + (bb // 2):
            size = self.bet_preflop(bb, pot)
        else:
            size = self.bet_after_preflop(pot)
        if not self.check_if_player_has_enough_money(stack, size):
            print("u dont have enough money")
            size = self.choose_size(bb, pot, stack)
        return size

    def bet(self, player, pot, enemy, bb):
        size = self.choose_size(bb, pot, player.stack)
        if player.stack == size:
            print("all in")
        player.stack -= size
        player.need_to_call = 0
        enemy.need_to_call += size
        pot += size
        return "raise", pot

    def call(self, player, pot):
        pot += player.need_to_call
        print(player.need_to_call)
        player.stack -= player.need_to_call
        player.need_to_call = 0
        return "call", pot

    def check(self, pot):
        return "check", pot

    def give_chips_to_the_winner(self, player, pot):
        player.stack += pot
        return f"The winner is {player.name}, his prize is {pot} and his stack is {player.stack}"
