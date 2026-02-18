from random import randint
from choices import UserInputChoices
from constantsa import UPPER_LIMIT_DEFAULT, LOWER_LIMIT_DEFAULT

class Game(object):
        
    # client_number:int|None = None

    def __init__(self, upper_limit:int=UPPER_LIMIT_DEFAULT, lower_limit:int=LOWER_LIMIT_DEFAULT) -> None:
        """
        Docstring for __init__
        
        :param self: Description
        :param upper_limit: Description
        :type upper_limit: int
        :param lower_limit: Description
        :type lower_limit: int
        """
        
        self._upper_limit:int = upper_limit
        self._lower_limit:int = lower_limit
        self.client_number = None
        self.guess_new_number()

    @property
    def upper_limit(self)->int:
        return self._upper_limit-1
    
    @upper_limit.setter
    def upper_limit(self, new_upper_limit:int):
        self._upper_limit = new_upper_limit

    @property
    def lower_limit(self)->int:
        return self._lower_limit+1
    
    @lower_limit.setter
    def lower_limit(self, new_lower_limit:int):
        self._upper_limit = new_lower_limit

    def guess_new_number(self):
        self.guessed_number = randint(self.lower_limit+1, self.upper_limit-1)

    def modify_in_lower_range(self):
        """
        Docstring for modify_in_lower_range
        ....
        """
        self.upper_limit = self.guessed_number

    def modify_in_upper_range(self):
        self.lower_limit = self.guessed_number

    def number_is_guessed(self):
        self.client_number = self.guessed_number

    def apply_user_input(self, user_input: UserInputChoices):
        if user_input == UserInputChoices.user_number_is_guessed:
            self.number_is_guessed()
            return
        elif user_input == UserInputChoices.user_number_is_higher:
            self.modify_in_upper_range()
        elif user_input == UserInputChoices.user_number_is_lower:
            self.modify_in_lower_range()
        self.guess_new_number()

    @property
    def is_game_finished(self):
        if self.client_number==self.guessed_number:
            return True
        return False

