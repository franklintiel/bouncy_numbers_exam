from constants import Constants
from functions import Functions
from messages import Messages


class BouncyNumberFinder:
    """
    The BouncyNumberFinder is a class that lets you know what is the lest number in proportion of bouncy numbers with a
    specific percentage
    """
    least_number: int = 0
    bouncy_counter: int = 0
    percentage_required: float = 0.00
    percentage: float = 0.00
    message: str = None

    def __init__(self, percentage_required: float = Constants.PERCENTAGE_REQUIRED):
        """
        Define the initial values with the class should be work
        :param percentage_required: percentage defined by the user when the class is called
        """
        self.percentage_required = percentage_required
        self.bouncy_counter = 0
        self.percentage = 0
        self.least_number = 0
        print(Messages.PROCESSING_MESSAGE.format(self.percentage_required))
        self.process()

    def __str__(self):
        """
        This function allow to return the message with the result from the process
        :return: the message with the result from the process
        """
        return self.message

    def get_percentage(self):
        """
        This function allow to calculate the percentage during the process
        :return: the percentage calculated
        """
        return round((self.bouncy_counter * 100) / self.least_number, Constants.DECIMALS_ALLOWED)

    def print_message(self):
        """
        This function allow to generate the success message
        :return:  the success message formatted.
        """
        self.message = Messages.SUCCESS_MESSAGES.format(self.least_number, self.percentage)

    def process(self):
        """
        This function allow to find the least number in proportion with the bouncy numbers found using as limit the
        percentage defined by the user.
        :return: This function return nothing
        """
        try:
            # if the percentage is negative or zero, so, send a ValueError exception
            if self.percentage_required <= Constants.PERCENTAGE_MINIMUM_REQUIRED:
                raise ValueError(Messages.PERCENTAGE_INVALID_MESSAGE)
            while self.percentage < self.percentage_required:
                self.least_number += 1
                # check if the number is a bouncy valid.
                is_bouncy: bool = Functions.is_bouncy_number(number=self.least_number)
                if is_bouncy is True:
                    self.bouncy_counter += 1
                self.percentage = self.get_percentage() # calculate the percentage
            self.print_message() # print the message with the result
        except ValueError as ex:
            self.message = str(ex)
        except Exception as ex:
            raise ex
