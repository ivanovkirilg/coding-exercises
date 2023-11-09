import enum
from dataclasses import dataclass, field

MINIMUM_LENGTH = 8
MINIMUM_NUMBERS_COUNT = 2


class ValidationError(enum.Enum):
    TOO_SHORT = 'Password must be at least 8 characters'
    TOO_FEW_NUMBERS = 'The password must contain at least 2 numbers'


@dataclass
class ValidationResult:
    is_valid: bool = True
    errors: list = field(default_factory=list)


VALIDATORS = {
    ValidationError.TOO_SHORT :
        lambda password: len(password) >= MINIMUM_LENGTH,
    ValidationError.TOO_FEW_NUMBERS :
        lambda password: _count_numbers(password) >= MINIMUM_NUMBERS_COUNT
}


def _count_numbers(password: str):
    return sum(char.isdigit() for char in password)

def validate(password):
    result = ValidationResult()

    for err, validator in VALIDATORS.items():
        if not validator(password):
            result.is_valid = False
            result.errors.append(err)

    return result