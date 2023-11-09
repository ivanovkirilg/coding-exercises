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


def _count_numbers(password: str):
    return sum(char.isdigit() for char in password)

def validate(password):
    result = ValidationResult()

    if len(password) < MINIMUM_LENGTH:
        result.is_valid = False
        result.errors.append(ValidationError.TOO_SHORT)

    if _count_numbers(password) < MINIMUM_NUMBERS_COUNT:
        result.is_valid = False
        result.errors.append(ValidationError.TOO_FEW_NUMBERS)

    return result
