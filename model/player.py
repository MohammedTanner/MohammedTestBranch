class Player:
    def __init__(self, whatPlayer):
        self.x = whatPlayer
        # symbol for corresponding values
        if whatPlayer == 1:
            self.symbol = "X"
        else:
            self.symbol = "O"
