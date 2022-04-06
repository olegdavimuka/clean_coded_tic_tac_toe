import random
import sys


class Game:
    computer_symbol = ""
    turns_count = 0

    def __init__(self, game_board, player):
        self.player = player
        self.game_board = game_board
        self.assign_symbol_to_computer()

    def assign_symbol_to_computer(self):
        self.computer_symbol = 'o' if self.player.player_symbol == "x" else "x"

    def make_computer_turn(self):
        turn = random.choice(self.game_board.free_fields)
        self.game_board.bound_fields[turn - 1] = self.computer_symbol

        self.game_board.free_fields.remove(turn)
        self.after_turn_actions()

    def handle_player_turn(self, player_turn):
        if not self.validate_player_turn_field_free(player_turn):
            return False

        self.game_board.bound_fields[player_turn - 1] = self.player.player_symbol
        self.game_board.free_fields.remove(player_turn)
        self.after_turn_actions()
        return True

    def after_turn_actions(self):
        self.turns_count += 1
        self.game_board.draw_field()
        if self.turns_count > 5:
            self.end_game_check()

    def validate_player_turn_field_free(self, turn_to_validate):
        if turn_to_validate not in self.game_board.free_fields:
            return False
        return True

    def play_game(self):  # TODO: Simplify
        if self.player.player_symbol == "x":
            for turns_count in range(0, 4):
                player_turn = self.player.make_player_turn("Make your turn, enter free field number between 1 and 9 : ")
                while not self.handle_player_turn(player_turn):
                    player_turn = self.player.make_player_turn(
                        "Make your turn, enter free field number between 1 and 9 : ")
                self.make_computer_turn()

            player_turn = self.player.make_player_turn("Make your turn, enter free field number between 1 and 9 : ")
            self.handle_player_turn(player_turn)
            while not self.handle_player_turn(player_turn):
                player_turn = self.player.make_player_turn(
                    "Make your turn, enter free field number between 1 and 9 : ")
        else:
            for turns_count in range(0, 4):
                self.make_computer_turn()
                player_turn = self.player.make_player_turn("Make your turn, enter free field number between 1 and 9 : ")
                while not self.handle_player_turn(player_turn):
                    player_turn = self.player.make_player_turn(
                        "Make your turn, enter free field number between 1 and 9 : ")
                self.handle_player_turn(player_turn)

            self.make_computer_turn()

    def end_game_check(self):
        for i in range(0, 3):
            if self.game_board.bound_fields[i] == self.game_board.bound_fields[i + 3] == \
                    self.game_board.bound_fields[i + 6] == self.player.player_symbol:
                self.winner_check(self.game_board.bound_fields[i])

        for i in range(0, 9, 3):
            if self.game_board.bound_fields[i] == self.game_board.bound_fields[i + 1] == \
                    self.game_board.bound_fields[i + 2] == self.player.player_symbol:
                self.winner_check(self.game_board.bound_fields[i])

        for i in (2, 4):
            if self.game_board.bound_fields[4 - i] == self.game_board.bound_fields[4] == \
                    self.game_board.bound_fields[4 + i] == self.player.player_symbol:
                self.winner_check(self.game_board.bound_fields[4])

        if self.turns_count == 9:
            print("It's a draw.")
            sys.exit(0)

    def winner_check(self, symbol):
        if symbol == self.player.player_symbol:
            print("Congratulations! You won!")
        else:
            print("Sad... you lose.")
        sys.exit(0)
