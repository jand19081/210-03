from game.terminal_service import TerminalService
from game.trooper import Trooper
from game.secret import Secret


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret: An instance of secret for storing guesses and the secret word.
        trooper: an instance of the trooper to be drawn based on the guesses.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret = Secret()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._trooper = Trooper()
        self._trooper.draw_trooper()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._secret.get_guess()
        self._terminal_service.write_text(guess)
        self._letter_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        correct = self._secret.check_geuss(self._letter_guess)
        
        if not correct:
            self._trooper.loose_point()
        
            
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        Alive = self._trooper.still_alive()
        win = self._check_win()
        
        if win == True:
                self._is_playing = False
                self._trooper.draw_trooper()
                self._terminal_service.write_text(self._secret.get_guess())
                self._terminal_service.write_text("You win!")
        elif Alive == False:
            self._trooper.draw_dead_trooper()
            self._terminal_service.write_text("You died.")
            self._is_playing = False
        else:
            self._trooper.draw_trooper()

    def _check_win(self):
        if self._secret.get_secret_word() == str(self._secret.get_guess()):
            return True
        else:
            return False