import enum
from dataclasses import dataclass

MINIMUM_LENGTH = 8


class ValidationError(enum.Enum):
    TOO_SHORT = 'Password must be at least 8 characters'


@dataclass
class ValidationResult:
    is_valid: bool
    errors: list


def validate(password):
    if len(password) < MINIMUM_LENGTH:
        return ValidationResult(
            False, [ValidationError.TOO_SHORT])
