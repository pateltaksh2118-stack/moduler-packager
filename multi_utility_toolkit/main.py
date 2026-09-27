"""
Multi-Utility Toolkit
---------------------
A menu-driven Python project demonstrating:

1. Built-in modules
2. Custom modules
3. Python packages
4. __name__ and __main__
5. dir() for dynamic module exploration
6. Date and time operations
7. Mathematical operations
8. Random data generation
9. UUID generation
10. File operations
"""

from toolkit.toolkit import datetime_utils
from toolkit.toolkit import math_utils
from toolkit.toolkit import random_utils
from toolkit.toolkit import file_utils


# ---------------------------------------------------------
# Common Utility Functions
# ---------------------------------------------------------

def print_header(title):
    """Display a formatted section heading."""
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


def get_integer(prompt, minimum=None, maximum=None):
    """Get a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a value less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter an integer.")


def get_float(prompt, minimum=None):
    """Get a valid floating-point number from the user."""
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a number.")


# ---------------------------------------------------------
# DATETIME AND TIME MENU
# ---------------------------------------------------------

def datetime_menu():
    """Display datetime and time operations."""
    while True:

        print_header("Datetime and Time Operations")

        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates/Times")
        print("3. Format Date Into Custom Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = get_integer("Enter your choice: ", 1, 6)

        # Current Date and Time
        if choice == 1:

            current = datetime_utils.current_datetime()

            print("\nCurrent Date and Time:")
            print(current)

        # Difference between dates
        elif choice == 2:

            first_date = input(
                "Enter first date/time (YYYY-MM-DD HH:MM:SS): "
            ).strip()

            second_date = input(
                "Enter second date/time (YYYY-MM-DD HH:MM:SS): "
            ).strip()

            try:

                difference = datetime_utils.date_time_difference(
                    first_date,
                    second_date
                )

                print("\nDifference:")
                print(difference)

            except ValueError:

                print(
                    "Invalid date/time format!"
                    "\nUse: YYYY-MM-DD HH:MM:SS"
                )

        # Custom date format
        elif choice == 3:

            date_text = input(
                "Enter date/time (YYYY-MM-DD HH:MM:SS): "
            ).strip()

            format_text = input(
                "Enter desired format "
                "(Example: %d-%m-%Y %I:%M %p): "
            ).strip()

            try:

                formatted_date = datetime_utils.format_datetime(
                    date_text,
                    format_text
                )

                print("\nFormatted Date:")
                print(formatted_date)

            except ValueError:

                print("Invalid date/time or format.")

        # Stopwatch
        elif choice == 4:

            elapsed = datetime_utils.run_stopwatch()

            print(f"\nElapsed Time: {elapsed:.2f} seconds")

        # Countdown
        elif choice == 5:

            seconds = get_integer(
                "Enter countdown time in seconds: ",
                1
            )

            datetime_utils.countdown(seconds)

        # Back
        elif choice == 6:

            break


# ---------------------------------------------------------
# MATHEMATICAL OPERATIONS MENU
# ---------------------------------------------------------

def math_menu():
    """Display mathematical operations."""
    while True:

        print_header("Mathematical Operations")

        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Calculate Logarithm")
        print("6. Back to Main Menu")

        choice = get_integer("Enter your choice: ", 1, 6)

        # Factorial
        if choice == 1:

            number = get_integer(
                "Enter a non-negative integer: ",
                0
            )

            try:

                result = math_utils.factorial(number)

                print(f"\nFactorial of {number}: {result}")

            except ValueError as error:

                print(f"Error: {error}")

        # Compound interest
        elif choice == 2:

            principal = get_float(
                "Enter principal amount: ",
                0
            )

            rate = get_float(
                "Enter annual interest rate (%): ",
                0
            )

            years = get_float(
                "Enter time in years: ",
                0
            )

            compounds = get_integer(
                "Enter number of compounds per year: ",
                1
            )

            try:

                amount, interest = math_utils.compound_interest(
                    principal,
                    rate,
                    years,
                    compounds
                )

                print(f"\nFinal Amount: {amount:.2f}")
                print(f"Compound Interest: {interest:.2f}")

            except ValueError as error:

                print(f"Error: {error}")

        # Trigonometry
        elif choice == 3:

            angle = get_float(
                "Enter angle in degrees: "
            )

            result = math_utils.trigonometry(angle)

            print(f"\nsin({angle}) = {result['sin']:.6f}")
            print(f"cos({angle}) = {result['cos']:.6f}")
            print(f"tan({angle}) = {result['tan']:.6f}")

        # Geometric shapes
        elif choice == 4:

            print("\nGeometric Shapes")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = get_integer(
                "Choose shape: ",
                1,
                3
            )

            if shape == 1:

                radius = get_float(
                    "Enter radius: ",
                    0
                )

                area = math_utils.circle_area(radius)

                print(f"\nArea of Circle: {area:.2f}")

            elif shape == 2:

                length = get_float(
                    "Enter length: ",
                    0
                )

                width = get_float(
                    "Enter width: ",
                    0
                )

                area = math_utils.rectangle_area(
                    length,
                    width
                )

                print(f"\nArea of Rectangle: {area:.2f}")

            elif shape == 3:

                base = get_float(
                    "Enter base: ",
                    0
                )

                height = get_float(
                    "Enter height: ",
                    0
                )

                area = math_utils.triangle_area(
                    base,
                    height
                )

                print(f"\nArea of Triangle: {area:.2f}")

        # Logarithm
        elif choice == 5:

            number = get_float(
                "Enter a positive number: ",
                0
            )

            base = get_float(
                "Enter logarithm base "
                "(Enter 0 for natural logarithm): ",
                0
            )

            try:

                if base == 0:

                    result = math_utils.natural_log(
                        number
                    )

                else:

                    result = math_utils.logarithm(
                        number,
                        base
                    )

                print(f"\nLogarithm: {result:.6f}")

            except ValueError as error:

                print(f"Error: {error}")

        # Back
        elif choice == 6:

            break


# ---------------------------------------------------------
# RANDOM DATA GENERATION MENU
# ---------------------------------------------------------

def random_menu():
    """Display random data generation options."""
    while True:

        print_header("Random Data Generation")

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")

        choice = get_integer(
            "Enter your choice: ",
            1,
            6
        )

        # Random number
        if choice == 1:

            minimum = get_integer(
                "Enter minimum value: "
            )

            maximum = get_integer(
                "Enter maximum value: "
            )

            try:

                number = random_utils.random_number(
                    minimum,
                    maximum
                )

                print(f"\nRandom Number: {number}")

            except ValueError:

                print(
                    "Minimum value cannot be greater "
                    "than maximum value."
                )

        # Random list
        elif choice == 2:

            size = get_integer(
                "Enter list size: ",
                1
            )

            minimum = get_integer(
                "Enter minimum value: "
            )

            maximum = get_integer(
                "Enter maximum value: "
            )

            try:

                values = random_utils.random_list(
                    size,
                    minimum,
                    maximum
                )

                print("\nRandom List:")
                print(values)

            except ValueError:

                print(
                    "Minimum value cannot be greater "
                    "than maximum value."
                )

        # Password
        elif choice == 3:

            length = get_integer(
                "Enter password length: ",
                4
            )

            try:

                password = random_utils.generate_password(
                    length
                )

                print(f"\nGenerated Password: {password}")

            except ValueError as error:

                print(f"Error: {error}")

        # OTP
        elif choice == 4:

            length = get_integer(
                "Enter OTP length: ",
                4
            )

            try:

                otp = random_utils.generate_otp(
                    length
                )

                print(f"\nGenerated OTP: {otp}")

            except ValueError as error:

                print(f"Error: {error}")

        # Sampling
        elif choice == 5:

            data = input(
                "Enter dataset values separated by spaces: "
            ).split()

            sample_size = get_integer(
                "Enter sample size: ",
                1
            )

            try:

                sample = random_utils.random_sample(
                    data,
                    sample_size
                )

                print("\nRandom Sample:")
                print(sample)

            except ValueError as error:

                print(f"Error: {error}")

        # Back
        elif choice == 6:

            break


# ---------------------------------------------------------
# UUID MENU
# ---------------------------------------------------------

def uuid_menu():
    """Generate a unique UUID4 identifier."""
    print_header("Generate Unique Identifier (UUID)")

    unique_id = random_utils.generate_uuid4()

    print("\nGenerated UUID4:")
    print(unique_id)


# ---------------------------------------------------------
# FILE OPERATIONS MENU
# ---------------------------------------------------------

def file_menu():
    """Display file operation options."""
    while True:

        print_header("File Operations (Custom Module)")

        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        choice = get_integer(
            "Enter your choice: ",
            1,
            5
        )

        # Create file
        if choice == 1:

            filename = input(
                "Enter file name: "
            ).strip()

            try:

                file_utils.create_file(filename)

                print("File created successfully!")

            except (ValueError, OSError) as error:

                print(f"Error: {error}")

        # Write file
        elif choice == 2:

            filename = input(
                "Enter file name: "
            ).strip()

            data = input(
                "Enter data to write: "
            )

            try:

                file_utils.write_file(
                    filename,
                    data
                )

                print("Data written successfully!")

            except (ValueError, OSError) as error:

                print(f"Error: {error}")

        # Read file
        elif choice == 3:

            filename = input(
                "Enter file name: "
            ).strip()

            try:

                content = file_utils.read_file(
                    filename
                )

                print("\nFile Content:")
                print(content)

            except (ValueError, OSError) as error:

                print(f"Error: {error}")

        # Append
        elif choice == 4:

            filename = input(
                "Enter file name: "
            ).strip()

            data = input(
                "Enter data to append: "
            )

            try:

                file_utils.append_file(
                    filename,
                    data
                )

                print("Data appended successfully!")

            except (ValueError, OSError) as error:

                print(f"Error: {error}")

        # Back
        elif choice == 5:

            break


# ---------------------------------------------------------
# DYNAMIC MODULE EXPLORATION
# ---------------------------------------------------------

def explore_module():
    """
    Explore the attributes of built-in and custom modules
    using Python's dir() function.
    """

    print_header("Explore Module Attributes (dir())")

    module_name = input(
        "Enter module name "
        "(math, random, datetime, uuid, "
        "math_utils, random_utils, datetime_utils, file_utils): "
    ).strip()

    modules = {

        "math": __import__("math"),

        "random": __import__("random"),

        "datetime": __import__("datetime"),

        "uuid": __import__("uuid"),

        "math_utils": math_utils,

        "random_utils": random_utils,

        "datetime_utils": datetime_utils,

        "file_utils": file_utils
    }

    module = modules.get(module_name)

    if module is None:

        print("\nModule not found.")

        print(
            "Please enter one of the supported module names."
        )

        return

    attributes = [
        item
        for item in dir(module)
        if not item.startswith("__")
    ]

    print(
        f"\nAvailable Attributes in "
        f"{module_name}:"
    )

    print(attributes)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():
    """Run the Multi-Utility Toolkit."""

    while True:

        print_header(
            "Welcome to Multi-Utility Toolkit"
        )

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = get_integer(
            "Enter your choice: ",
            1,
            7
        )

        if choice == 1:

            datetime_menu()

        elif choice == 2:

            math_menu()

        elif choice == 3:

            random_menu()

        elif choice == 4:

            uuid_menu()

        elif choice == 5:

            file_menu()

        elif choice == 6:

            explore_module()

        elif choice == 7:

            print_header("Exit")

            print(
                "Thank you for using the "
                "Multi-Utility Toolkit!"
            )

            break


# ---------------------------------------------------------
# __name__ and __main__ Demonstration
# ---------------------------------------------------------

if __name__ == "__main__":
    main()