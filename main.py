from Objects.Player import player
from DatabaseConnections.OracleDB import getData



data = getData("player", "*", "player_id = :id", {"id": 1})
for row in data:
    print(row)
