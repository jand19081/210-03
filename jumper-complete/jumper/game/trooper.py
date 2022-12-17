from game.terminal_service import TerminalService


class Trooper():
    """An instance of Trooper.
        
        Attributes:
            trooper: The trooper to be drawn.
    """

    def __init__(self):
        """An instance of trooper."""
        self._terminal_service = TerminalService()
        self._wrong_guesses = 0
        self._trooper = {
            "row1": ["  ___  "],
            "row2": [" /___\ "],
            "row3": [" \   / "],
            "row4": ["  \ /  "],
            "row5": ["   0   "],
            "row6": ["  /|\  "],
            "row7": ["  / \  "]
            }

    def loose_point(self):
        self._wrong_guesses += 1
        
        row = "row" + str(self._wrong_guesses)
        self._trooper[row] = ["       "]

    def still_alive(self):
        if self._wrong_guesses < 4:
            return True
        else:
            return False

    def draw_trooper(self):
        keys = ["row1", "row2", "row3", "row4", "row5", "row6", "row7"]
        for key in keys:
            row = str(self._trooper[key][0])
            self._terminal_service.write_text(row)

    def draw_dead_trooper(self):
        self._trooper = {
            "row1": ["       "],
            "row2": ["       "],
            "row3": ["       "],
            "row4": ["       "],
            "row5": ["   x   "],
            "row6": ["  /|\  "],
            "row7": ["  / \  "]
            }

        keys = ["row1", "row2", "row3", "row4", "row5", "row6", "row7"]
        for key in keys:
            row = str(self._trooper[key][0])
            self._terminal_service.write_text(row)