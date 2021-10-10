from game.dealer import Dealer
import time
from colorama import Back,init
init(autoreset=True)

print(Back.BLUE +"Hi, Welcome to our Game")
time.sleep(0.7)

class Director:
    """A code template for a person who directs the game. 
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points.
        dealer (Dealer): An instance of the class of objects known as dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_output_1()
            self.do_updates()
            self.do_output_2()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        self.dealer.throw_dice()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points()
        self.score += points
        self.dealer.score = self.score
        
    def do_output_1(self):
        """Outputs the first half of game information for each round of play.
        Args:
            self (Director): An instance of Director.
        """
        
        print(f"\nThe card is: {self.dealer.dice[0]}")
        another = input("Higher or lower? [h/l] ")
        self.dealer.answer = another
        print(f"\nNext card was: {self.dealer.dice[1]}")

    def do_output_2(self):
        """Outputs the second half game information for each round of play.
        After answer the Higher or Lower question.  

        Args:
            self (Director): An instance of Director.
        """
        time.sleep(0.7)
        print(f"Your score is: {self.score}")
        if self.dealer.can_throw():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            print(Back.BLUE +"Thanks for playing!!!")
            self.keep_playing = False