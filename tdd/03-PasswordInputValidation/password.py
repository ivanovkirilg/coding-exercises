from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    errors: list

MINIMUM_LENGTH = 8

def validate(password):
    if len(password) < MINIMUM_LENGTH:
        return ValidationResult(
            False, ['Password must be at least 8 characters'])
