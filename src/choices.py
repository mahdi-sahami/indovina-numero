from enum import StrEnum

class UserInputChoices(StrEnum):
    user_number_is_lower = "lower"
    user_number_is_guessed = "is"
    user_number_is_higher = "upper"
    

    @classmethod
    def get_all_visible_choices(cls)->str:
        return f"{cls.user_number_is_guessed}, {cls.user_number_is_higher}, {cls.user_number_is_lower}"