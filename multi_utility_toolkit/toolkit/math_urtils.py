"""
Mathematical Utilities

This custom module demonstrates the use of
Python's math module.
"""

import math


def factorial(number):
    """
    Calculate factorial of a number.
    """

    if not isinstance(
        number,
        int
    ):

        raise ValueError(
            "Factorial requires an integer."
        )

    if number < 0:

        raise ValueError(
            "Factorial cannot be negative."
        )

    return math.factorial(
        number
    )


def compound_interest(
    principal,
    annual_rate,
    years,
    compounds_per_year=1
):
    """
    Calculate compound interest.

    Returns:
        amount
        interest
    """

    if principal < 0:
        raise ValueError(
            "Principal cannot be negative."
        )

    if annual_rate < 0:
        raise ValueError(
            "Interest rate cannot be negative."
        )

    if years < 0:
        raise ValueError(
            "Time cannot be negative."
        )

    if compounds_per_year <= 0:
        raise ValueError(
            "Compounds per year must be positive."
        )

    rate = annual_rate / 100

    amount = principal * (
        1 + rate / compounds_per_year
    ) ** (
        compounds_per_year * years
    )

    interest = (
        amount - principal
    )

    return amount, interest


def trigonometry(angle_degrees):
    """
    Calculate sine, cosine and tangent.

    Input angle is provided in degrees.
    """

    radians = math.radians(
        angle_degrees
    )

    return {
        "sin": math.sin(radians),
        "cos": math.cos(radians),
        "tan": math.tan(radians)
    }


def circle_area(radius):
    """
    Calculate the area of a circle.
    """

    if radius < 0:
        raise ValueError(
            "Radius cannot be negative."
        )

    return math.pi * radius ** 2


def rectangle_area(
    length,
    width
):
    """
    Calculate the area of a rectangle.
    """

    if length < 0 or width < 0:
        raise ValueError(
            "Dimensions cannot be negative."
        )

    return length * width


def triangle_area(
    base,
    height
):
    """
    Calculate the area of a triangle.
    """

    if base < 0 or height < 0:
        raise ValueError(
            "Dimensions cannot be negative."
        )

    return 0.5 * base * height


def natural_log(number):
    """
    Calculate natural logarithm.
    """

    if number <= 0:

        raise ValueError(
            "Number must be greater than zero."
        )

    return math.log(
        number
    )


def logarithm(
    number,
    base
):
    """
    Calculate logarithm using
    a specified base.
    """

    if number <= 0:

        raise ValueError(
            "Number must be greater than zero."
        )

    if base <= 0 or base == 1:

        raise ValueError(
            "Base must be positive "
            "and cannot be 1."
        )

    return math.log(
        number,
        base
    )