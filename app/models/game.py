from app.models.player import *


class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    player1 = Player("John", "Rock")
    player2 = Player("Mike", "Scissors")
    player3 = Player("Phil", "Paper")


    def get_the_winner(player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return player_1
            
        if player_1.choice == "Scissors" and player_2.choice == "Paper":
            return player_1
            
        if player_1.choice == "Paper" and player_2.choice == "Rock":
            return player_1

        if player_1.choice == player_2.choice:
            return None

        
        return player_2