'''
Create a function that can be used as a validator for the password field
of a user registration form. The validation function takes a string as
an input and returns a validation result. The validation result should contain
a boolean indicating if the password is valid or not, and also a field
with the possible validation errors.
'''

import password

import unittest

def _build_password(min_length  = password.MINIMUM_LENGTH,
                    nr_numbers  = password.MINIMUM_NUMBERS_COUNT,
                    nr_capitals = password.MINIMUM_CAPITAL_LETTERS_COUNT,
                    nr_specials = password.MINIMUM_SPECIAL_CHARACTERS_COUNT):
    pw = '1' * nr_numbers + 'A' * nr_capitals + '.' * nr_specials
    nr_lower = min_length - len(pw)
    pw += 'a' * nr_lower
    return pw

class TestPasswordValidate(unittest.TestCase):
    def test_valid_password(self):
        '''
        The password must be at least 8 characters long.
        The password must contain at least 2 numbers.
        The password must contain at least one capital letter.
        The password must contain at least one special character.
        '''
        pw = _build_password()

        result = password.validate(pw)

        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.errors), 0)

    def test_error_when_password_too_short(self):
        '''
        The password must be at least 8 characters long.
        If it is not met, then the following error message should be returned:
        “Password must be at least 8 characters”
        '''
        pw = _build_password(min_length=password.MINIMUM_LENGTH - 1)

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_SHORT, result.errors)

    def test_error_when_not_enough_numbers(self):
        '''
        The password must contain at least 2 numbers.
        If it is not met, then the following error message should be returned:
        “The password must contain at least 2 numbers”
        '''
        pw = _build_password(nr_numbers=password.MINIMUM_NUMBERS_COUNT - 1)

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_FEW_NUMBERS, result.errors)

    def test_error_when_not_enough_capital_letters(self):
        '''
        The password must contain at least one capital letter.
        If it is not met, then the following error message should be returned:
        “password must contain at least one capital letter”
        '''
        pw = _build_password(
            nr_capitals=password.MINIMUM_CAPITAL_LETTERS_COUNT - 1)

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
        pw = _build_password(
            min_length=password.MINIMUM_LENGTH - 1,
            nr_numbers=password.MINIMUM_CAPITAL_LETTERS_COUNT - 1)

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_SHORT, result.errors)
        self.assertIn(password.ValidationError.TOO_FEW_NUMBERS, result.errors)

    def test_error_when_not_enough_special_characters(self):
        '''
        The password must contain at least one special character.
        If it is not met, then the following error message should be returned:
        “Password must contain at least one special character”
        '''
        pw = _build_password(
            nr_specials=password.MINIMUM_SPECIAL_CHARACTERS_COUNT - 1)

        result = password.validate(pw)

        self.assertFalse(result.is_valid)
        self.assertIn(password.ValidationError.TOO_FEW_SPECIAL_CHARACTERS,
                      result.errors)


if __name__ == '__main__':
    unittest.main()
