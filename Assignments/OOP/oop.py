class NFLTeam :
    def __init__(self, teamName, playerList) :
        self.teamName = teamName
        self.playerList = playerList

class Player :
    def __init__(self, playerName, playerPosition) :
        self.playerName = playerName
        self.playerPosition = playerPosition

player1 = Player ("Joe Montana", "QB")
player2 = Player ("Barry Sanders", "RB")
player3 = Player ("Jerry Rice", "WR")
player4 = Player ("Graham Grano", "K")


playerList = [player1, player2, player3, player4]
teamName = "RedHunters"

print("NFL Team: ", teamName)
print("")
print(player1.playerName, player1.playerPosition)
print(player2.playerName, player2.playerPosition)
print(player3.playerName, player3.playerPosition)
print(player4.playerName, player4.playerPosition)

