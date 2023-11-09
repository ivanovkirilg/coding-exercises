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
        pw = 'hi'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_SHORT, result.errors)

    def test_error_when_not_enough_numbers(self):
        '''
        The password must contain at least 2 numbers.
        If it is not met, then the following error message should be returned:
        “The password must contain at least 2 numbers”
        '''
        pw = 'abcdefghij'

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_FEW_NUMBERS, result.errors)


if __name__ == '__main__':
    unittest.main()
