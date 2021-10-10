import random
from colorama import Back,Fore,init
init(autoreset=True)

class Dealer:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        dice (list): 
        answer (list):
        score (number): 
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of Director.
        """
        self.list = []
        self.answer = []
        self.score = 0

    def can_throw(self):
        """Determines how many times the dealer will 
        show a card. If the score reaches 0, returns a False.
        
        Args:
            self (Thrower): an instance of Director.
        """
        if self.score <= 0:
            print(Back.BLUE +"Thanks for playing!!!")
            return False
        else:
            self.dice.clear()
            return True

    def get_points(self):
        """Calculates and returns the total points for the current
        turn. Correct answers are worth 100 points. Wrong answers 
        are worth -75 points.
        
        Args:
            self (Thrower): an instance of Director.
        """
        if self.answer == "h" and self.list[1] > self.list[0]:
            print(Fore.GREEN +"😃"+"😃"+" "+"Good!!!!!!!")
            return 100
            
        elif self.answer == "l" and self.list[1] < self.list[0]:
            print(Fore.GREEN +"😃"+"😃"+" "+"Good!!!!!!!")
            return 100
            
        else:
            print(Fore.RED +"☹"+"☹"+" "+ "Fail!!!!!!!")
            return -75

    def throw_dice(self):
        """Randomly generates two new values and adds them 
        to the list. 
        
        Args:
            self (Thrower): an instance of Director.
        """
        for x in range(2):
            one = random.randint(1, 13)
            self.list.append(one)