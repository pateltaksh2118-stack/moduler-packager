"""
Random Data Utilities

This module demonstrates:
- random
- string
- uuid
"""

import random
import string
import uuid


def random_number(
    lower,
    upper
):
    """
    Generate a random integer.
    """

    if lower > upper:

        raise ValueError(
            "Lower value cannot be "
            "greater than upper value."
        )

    return random.randint(
        lower,
        upper
    )


def random_list(
    size,
    lower,
    upper
):
    """
    Generate a random list of integers.
    """

    if size <= 0:

        raise ValueError(
            "List size must be positive."
        )

    if lower > upper:

        raise ValueError(
            "Lower value cannot be "
            "greater than upper value."
        )

    values = []

    for _ in range(size):

        value = random.randint(
            lower,
            upper
        )

        values.append(value)

    return values


def generate_password(length):
    """
    Generate a random password containing:
    letters, numbers and symbols.
    """

    if length < 4:

        raise ValueError(
            "Password length must be "
            "at least 4."
        )

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for _ in range(length):

        password += random.choice(
            characters
        )

    return password


def generate_otp(length=6):
    """
    Generate a random numeric OTP.
    """

    if length < 4:

        raise ValueError(
            "OTP length must be "
            "at least 4."
        )

    digits = string.digits

    otp = ""

    for _ in range(length):

        otp += random.choice(
            digits
        )

    return otp


def random_sample(
    data,
    sample_size
):
    """
    Select random values from a dataset
    without replacement.
    """

    if sample_size <= 0:

        raise ValueError(
            "Sample size must be positive."
        )

    if sample_size > len(data):

        raise ValueError(
            "Sample size cannot be greater "
            "than dataset size."
        )

    return random.sample(
        data,
        sample_size
    )


def generate_uuid4():
    """
    Generate a UUID version 4.
    """

    return str(
        uuid.uuid4()
    )