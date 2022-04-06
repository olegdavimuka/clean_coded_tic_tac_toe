from game import Game
from game_board import GameBoard
from player import Player

game_board = GameBoard()
player = Player()
game = Game(game_board, player)
game.play_game()
