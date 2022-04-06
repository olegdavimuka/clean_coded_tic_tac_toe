class Player:
    player_symbol = ""

    def __init__(self):
        self.choice_symbol_to_play()

    def choice_symbol_to_play(self):
        player_input = input("Choose X or O: ")
        return self.validate_player_input(player_input)

    def validate_player_input(self, player_input):
        if player_input.lower() != "x" and player_input.lower() != "o":
            self.choice_symbol_to_play()
            return
        self.player_symbol = player_input

    def make_player_turn(self, message):
        player_turn = self.convert_to_int(input(message))
        while not self.validate_player_turn(player_turn):
            return self.make_player_turn("Please enter a number between 1 and 9, which represents free field:")
        return player_turn

    def validate_player_turn(self, turn_to_validate):
        if not self.validate_player_turn_type(turn_to_validate):
            return False
        if not self.validate_player_turn_range(turn_to_validate):
            return False
        return True

    @staticmethod
    def validate_player_turn_type(turn_to_validate):
        if type(turn_to_validate) != int:
            return False
        return True

    @staticmethod
    def validate_player_turn_range(turn_to_validate):
        if turn_to_validate not in range(1, 10):
            return False
        return True

    @staticmethod
    def convert_to_int(string_to_be_converted):
        try:
            int(string_to_be_converted)
            return int(string_to_be_converted)
        except ValueError:
            return string_to_be_converted
