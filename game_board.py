class GameBoard:
    free_fields = list(range(1, 10))
    bound_fields = [" "] * 9

    def draw_field(self):
        print(f"     |     |     \n"
              f"  {self.bound_fields[0]}  |  {self.bound_fields[1]}  |  {self.bound_fields[2]}  \n"
              f"     |     |     \n"
              f"----- ----- -----\n"
              f"     |     |     \n"
              f"  {self.bound_fields[3]}  |  {self.bound_fields[4]}  |  {self.bound_fields[5]}  \n"
              f"     |     |     \n"
              f"----- ----- -----\n"
              f"     |     |     \n"
              f"  {self.bound_fields[6]}  |  {self.bound_fields[7]}  |  {self.bound_fields[8]}  \n"
              f"     |     |     \n")
