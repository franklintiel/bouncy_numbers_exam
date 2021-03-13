from unittest import TestCase, main
from models import Functions, BouncyNumberFinder


class FunctionTestCase(TestCase):
    """
    Unit Tests defined to validate the logic applied in the Functions class.
    """

    def test_is_bouncy_number_function_params_valid(self):
        """
        Unit test applied when the parameter is a valid bouncy number
        :return:
        """
        is_valid: bool = Functions.is_bouncy_number(number=101)
        self.assertTrue(is_valid)

    def test_is_bouncy_number_function_params_invalid(self):
        """
        Unit test applied when the parameter is an invalid bouncy number
        :return:
        """
        is_valid: bool = Functions.is_bouncy_number(number=119)
        self.assertFalse(is_valid)

    def test_is_bouncy_number_function_params_invalid_least_one_hundred(self):
        """
        Unit test applied when the parameter is an invalid bouncy number (less to 100)
        :return:
        """
        is_valid: bool = Functions.is_bouncy_number(number=99)
        self.assertFalse(is_valid)

    def test_is_bouncy_number_function_params_invalid_chars_value(self):
        """
        Unit test applied when the parameter is invalid type
        :return:
        """
        with self.assertRaises(TypeError):
            is_valid: bool = Functions.is_bouncy_number(number="value")

    def test_is_bouncy_number_function_params_invalid_boolean_value(self):
        """
        Unit test applied when the parameter is invalid type
        :return:
        """
        is_valid: bool = Functions.is_bouncy_number(number=True)
        self.assertFalse(is_valid)


class BouncyNumberFinderTestCase(TestCase):
    """
    Unit Tests defined to validate the logic applied in the BouncyNumberFinder class
    """

    def test_get_proportion_least_number_with_invalid_params_chart_percentage(self):
        """
        Unit test applied when the percentage parameter is an invalid value type
        :return:
        """
        with self.assertRaises(TypeError):
            instance = BouncyNumberFinder(percentage_required="value")

    def test_get_proportion_least_number_with_0_percentage(self):
        """
        Unit test applied when the percentage required is zero
        :return:
        """
        instance = BouncyNumberFinder(percentage_required=0)
        self.assertEqual(instance.percentage, 0)
        self.assertEqual(instance.least_number, 0)
        self.assertEqual(instance.message, "The percentage required to test should be greater zero")
        self.assertEqual(instance.__str__(), "The percentage required to test should be greater zero")

    def test_get_proportion_least_number_with_5_percentage(self):
        """
        Unit test applied when the percentage required is 5
        :return:
        """
        instance = BouncyNumberFinder(percentage_required=5)
        self.assertEqual(instance.percentage, 5.66)
        self.assertEqual(instance.least_number, 106)
        self.assertEqual(instance.message,
                         "Process Complete!. "
                         "The least number is 106 with bouncy numbers' proportion equal to 5.66%")
        self.assertEqual(instance.__str__(),
                         "Process Complete!. "
                         "The least number is 106 with bouncy numbers' proportion equal to 5.66%")

    def test_get_proportion_least_number_with_50_percentage(self):
        """
        Unit test applied when the percentage required is 50
        :return:
        """
        instance = BouncyNumberFinder(percentage_required=50)
        self.assertEqual(instance.percentage, 50.00)
        self.assertEqual(instance.least_number, 538)
        self.assertEqual(instance.message,
                         "Process Complete!. "
                         "The least number is 538 with bouncy numbers' proportion equal to 50.0%")
        self.assertEqual(instance.__str__(),
                         "Process Complete!. "
                         "The least number is 538 with bouncy numbers' proportion equal to 50.0%")

    def test_get_proportion_least_number_with_90_percentage(self):
        """
        Unit test applied when the percentage required is 90
        :return:
        """
        instance = BouncyNumberFinder(percentage_required=90)
        self.assertEqual(instance.percentage, 90.00)
        self.assertEqual(instance.least_number, 21770)
        self.assertEqual(instance.message,
                         "Process Complete!. "
                         "The least number is 21770 with bouncy numbers' proportion equal to 90.0%")
        self.assertEqual(instance.__str__(),
                         "Process Complete!. "
                         "The least number is 21770 with bouncy numbers' proportion equal to 90.0%")

    def test_get_proportion_least_number_with_99_percentage(self):
        """
        Unit test applied when the percentage required is 5
        :return:
        """
        instance = BouncyNumberFinder(percentage_required=99)
        self.assertEqual(instance.percentage, 99.00)
        self.assertEqual(instance.least_number, 1577612)
        self.assertEqual(instance.message,
                         "Process Complete!. "
                         "The least number is 1577612 with bouncy numbers' proportion equal to 99.0%")
        self.assertEqual(instance.__str__(),
                         "Process Complete!. "
                         "The least number is 1577612 with bouncy numbers' proportion equal to 99.0%")


# The following lines are required to run the unit tests with the commands:
# python -m unittest tests.py
# coverage run -m unittest tests.py && coverage report
if __name__ == '__main__':
    main()
# NOTICE: If you want generate the coverage HTML report, so, run the following command:
# coverage run -m unittest tests.py && coverage report && coverage html
