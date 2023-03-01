from django.core.exceptions import ValidationError


def not_false(value: bool):
    if value:
        raise ValidationError(f"can't use {value}")
