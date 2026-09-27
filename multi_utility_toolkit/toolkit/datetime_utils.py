"""
Datetime and Time Utilities

This custom module demonstrates the use of:
- datetime
- time
- strftime
- timedelta
"""

import time
from datetime import datetime


# Standard date and time format
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def current_datetime():
    """
    Return the current date and time.
    """

    current = datetime.now()

    return current.strftime(
        DATETIME_FORMAT
    )


def parse_datetime(date_text):
    """
    Convert string into datetime object.
    """

    return datetime.strptime(
        date_text,
        DATETIME_FORMAT
    )


def date_time_difference(
    first_text,
    second_text
):
    """
    Calculate absolute difference between
    two date/time values.
    """

    first = parse_datetime(
        first_text
    )

    second = parse_datetime(
        second_text
    )

    difference = abs(
        second - first
    )

    return difference


def format_datetime(
    date_text,
    format_text
):
    """
    Convert a date/time into a
    custom user-defined format.
    """

    date_value = parse_datetime(
        date_text
    )

    return date_value.strftime(
        format_text
    )


def run_stopwatch():
    """
    Run a simple stopwatch.

    The stopwatch starts when the user
    presses Enter and stops when the
    user presses Enter again.
    """

    input(
        "Press Enter to start the stopwatch..."
    )

    start_time = time.perf_counter()

    input(
        "Stopwatch running... "
        "Press Enter to stop."
    )

    end_time = time.perf_counter()

    elapsed_time = (
        end_time - start_time
    )

    return elapsed_time


def countdown(seconds):
    """
    Run a countdown timer.
    """

    print("\nCountdown Started...")

    for remaining in range(
        seconds,
        0,
        -1
    ):

        print(
            f"\rTime Remaining: "
            f"{remaining:3d} seconds",
            end="",
            flush=True
        )

        time.sleep(1)

    print(
        "\rTime Remaining:   0 seconds"
    )

    print("Countdown Finished!")