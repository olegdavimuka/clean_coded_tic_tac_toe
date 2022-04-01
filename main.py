import random
import sys

player_choice_xo = ""
computer_choice_xo = ""
turns_made = [" "] * 9
is_over = False
winner = 0


def player_choice():
    global player_choice_xo, computer_choice_xo
    player_choice_xo = input("Choose X or O: ")
    while player_choice_xo.lower() != "x" and player_choice_xo.lower() != "o":
        player_choice_xo = input("Please, enter X or O: ")

    computer_choice_xo = "o" if player_choice_xo == "x" else computer_choice_xo = "x"


def draw_field(turns):
    print(f"     |     |     \n"
          f"  {turns[0]}  |  {turns[1]}  |  {turns[2]}  \n"
          f"     |     |     \n"
          f"----- ----- -----\n"
          f"     |     |     \n"
          f"  {turns[3]}  |  {turns[4]}  |  {turns[5]}  \n"
          f"     |     |     \n"
          f"----- ----- -----\n"
          f"     |     |     \n"
          f"  {turns[6]}  |  {turns[7]}  |  {turns[8]}  \n"
          f"     |     |     \n")


def player_turn():
    end_game_check()
    win_check(2)

    while True:
        try:
            turn = input("Make your turn (enter free field number between 1 and 9) : ")
            int(turn)
            break
        except ValueError:
            print("Please, enter a NUMBER.")

    while not (9 >= int(turn) >= 1 and turns_made[int(turn) - 1] == " "):
        turn = input("Please, enter free field number between 1 and 9: ")

    turns_made[int(turn) - 1] = player_choice_xo
    draw_field(turns_made)


def computer_turn():
    end_game_check()
    win_check(1)

    turn = random.randint(1, 9)
    while not turns_made[turn - 1] == " ":
        turn = random.randint(1, 9)

    turns_made[int(turn) - 1] = computer_choice_xo
    print("Computer Turn:\n")
    draw_field(turns_made)


def end_game_check():
    for turn in turns_made:
        if turn == " ":
            return

    winner_check(0)


def win_check(player):
    global winner

    if turns_made[0] == turns_made[3] == turns_made[6] != " " \
            or turns_made[1] == turns_made[4] == turns_made[7] != " " \
            or turns_made[2] == turns_made[5] == turns_made[8] != " " \
            or turns_made[0] == turns_made[1] == turns_made[2] != " " \
            or turns_made[3] == turns_made[4] == turns_made[5] != " " \
            or turns_made[6] == turns_made[7] == turns_made[8] != " " \
            or turns_made[0] == turns_made[4] == turns_made[8] != " " \
            or turns_made[2] == turns_made[4] == turns_made[6] != " ":
        winner_check(player)


def winner_check(player):
    if player == 0:
        print("It's a draw.")
    elif player == 1:
        print("Congratulations! You won!")
    else:
        print("Sad... you lose.")
    sys.exit(0)


# G A M E
player_choice()
if player_choice_xo == "x":
    while True:
        player_turn()
        computer_turn()
else:
    while True:
        computer_turn()
        player_turn()
