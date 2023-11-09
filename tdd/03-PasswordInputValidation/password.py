import enum
from dataclasses import dataclass, field

MINIMUM_LENGTH = 8
MINIMUM_NUMBERS_COUNT = 2
MINIMUM_CAPITAL_LETTERS_COUNT = 1


class ValidationError(enum.Enum):
    TOO_SHORT = 'Password must be at least 8 characters'
    TOO_FEW_NUMBERS = 'The password must contain at least 2 numbers'
    TOO_FEW_CAPITAL_LETTERS = 'Password must contain at least one capital letter'

@dataclass
class ValidationResult:
    is_valid: bool = True
    errors: list = field(default_factory=list)


VALIDATORS = {
    ValidationError.TOO_SHORT :
        lambda password: len(password) >= MINIMUM_LENGTH,
    ValidationError.TOO_FEW_NUMBERS :
        lambda password: _count(password, str.isdigit) >= MINIMUM_NUMBERS_COUNT,
    ValidationError.TOO_FEW_CAPITAL_LETTERS :
        lambda password:
            _count(password, str.isupper) >= MINIMUM_CAPITAL_LETTERS_COUNT
}



def _count(password: str, checker: callable):
    return sum(checker(char) for char in password)

def validate(password):
    result = ValidationResult()

    for err, validator in VALIDATORS.items():
        if not validator(password):
            result.is_valid = False
            result.errors.append(err)

    return result
