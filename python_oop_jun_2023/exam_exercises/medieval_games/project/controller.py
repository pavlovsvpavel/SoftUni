from collections import deque
from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = [
        "Food",
        "Drink"
    ]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def __valid_player(self, player_name: str):
        try:
            current_player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return

        return current_player

    def add_player(self, *players) -> str:
        added_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f'Successfully added: {", ".join(added_players)}'

    def add_supply(self, *supplies) -> None:
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.__valid_player(player_name)

        if sustenance_type not in Controller.VALID_TYPES or not current_player:
            return

        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        try:
            pos, current_supply = [(pos, s) for pos, s in enumerate(self.supplies)
                                   if s.__class__.__name__ == sustenance_type][-1]
        except IndexError:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if current_player.stamina + current_supply.energy > 100:
            current_player.stamina = 100
        else:
            current_player.stamina += current_supply.energy

        del self.supplies[pos]

        return f"{player_name} sustained successfully with {current_supply.name}."

    @staticmethod
    def __stamina_check(stamina) -> int:
        if stamina <= 0:
            return 0

        return stamina

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_p = self.__valid_player(first_player_name)
        second_p = self.__valid_player(second_player_name)

        messages = []
        for p in [first_p, second_p]:
            if p.stamina == 0:
                messages.append(f"Player {p.name} does not have enough stamina.")

        if messages:
            return "\n".join(messages)

        players = deque(sorted([first_p, second_p], key=lambda x: x.stamina))

        counter = 0

        while counter < 2:

            attacker = players[0]
            defender = players[1]

            reduce_stamina = attacker.stamina / 2

            defender.stamina = self.__stamina_check(defender.stamina - reduce_stamina)

            if defender.stamina == 0:
                messages.append(f"Winner: {attacker.name}")
                break

            counter += 1
            players.rotate()

        winner = sorted([first_p, second_p], key=lambda x: -x.stamina)[0]

        return f"Winner: {winner.name}"

    def next_day(self) -> None:
        for p in self.players:
            reduce_stamina = p.age * 2
            p.stamina = self.__stamina_check(p.stamina - reduce_stamina)

        for p in self.players:
            for sustain in Controller.VALID_TYPES:
                self.sustain(p.name, sustain)

    def __str__(self) -> str:
        result = []
        for p in self.players:
            result.append(str(p))

        for s in self.supplies:
            result.append(s.details())

        return "\n".join(result)
