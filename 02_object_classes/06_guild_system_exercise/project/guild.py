from typing import List
from project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."  # player.name
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."  # player.name
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"  # player.name

    def kick_player(self, player_name: str):
        for player in self.players:
            if player_name == player:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return "\n".join([f"Guild: {self.name}"] + [player.player_info() for player in self.players])
        # info = [f"Guild: {self.name}"]
        # for player in self.players:
        #     info.append(player.player_info())
        # return '\n'.join(info)


# test code:

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
