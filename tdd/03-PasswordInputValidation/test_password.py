'''
Create a function that can be used as a validator for the password field
of a user registration form. The validation function takes a string as
an input and returns a validation result. The validation result should contain
a boolean indicating if the password is valid or not, and also a field
with the possible validation errors.
'''

import password

import unittest

class TestPasswordValidate(unittest.TestCase):
    def test_error_when_password_too_short(self):
        '''
        The password must be at least 8 characters long.
        If it is not met, then the following error message should be returned:
        “Password must be at least 8 characters”
        '''
        pw = 'A12.'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_SHORT, result.errors)

    def test_error_when_not_enough_numbers(self):
        '''
        The password must contain at least 2 numbers.
        If it is not met, then the following error message should be returned:
        “The password must contain at least 2 numbers”
        '''
        pw = 'Abcdefghij.'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_FEW_NUMBERS, result.errors)

    def test_error_when_not_enough_capital_letters(self):
        '''
        The password must contain at least one capital letter.
        If it is not met, then the following error message should be returned:
        “password must contain at least one capital letter”
        '''
        pw = 'abcdefgh12.'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_FEW_CAPITAL_LETTERS,
                      result.errors)

    def test_multiple_errors_recognized(self):
        '''
        The validation function should handle multiple validation errors.
        For example, “somepassword” should an error message:
        “Password must be at least 8 characters
        The password must contain at least 2 numbers”
        '''
        pw = 'hi'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_SHORT, result.errors)
        self.assertIn(password.ValidationError.TOO_FEW_NUMBERS, result.errors)


if __name__ == '__main__':
    unittest.main()
