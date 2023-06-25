from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player_name: Player) -> str:
        if player_name.guild == self.name:
            return f"Player {player_name.name} is already in the guild."

        if player_name.guild != Player.DEFAULT_GUILD:
            return f"Player {player_name.name} is in another guild."

        self.players.append(player_name)
        player_name.guild = self.name

        return f"Welcome player {player_name.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            c_player = next(filter(lambda x: x.name == player_name, self.players))

        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(c_player)
        c_player.guild = Player.DEFAULT_GUILD

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = []
        for current_player in self.players:
            result.append(f"{current_player.player_info()}")

        return f"Guild: {self.name}\n" + \
            f"".join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
