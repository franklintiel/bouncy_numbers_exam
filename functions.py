from constants import Constants


class Functions:
    """
    This class allow define static functions can be used in the script
    """

    @staticmethod
    def is_bouncy_number(number: int):
        """
        This function allow to valid if the number tested is a valid bouncy number
        :param number:
        :return:  True if is a valid number else return False
        """
        if number < Constants.FIRST_BOUNCY_NUMBER: # Check if the number is less to 100
            return False
        chars_list: str = list(str(number)) # Generate a chars list from the number tested
        increasing_list: str = sorted(str(number)) # Generate a ascending list from the chars list
        reverse_list = chars_list[::-1] # Generate a inverted or reverse list from the chars list
        # If the ascending list is diff to chars list and
        # the ascending list is diff to reverse on inverted list the is a valid bouncy number
        return True if increasing_list != chars_list and increasing_list != reverse_list else False
