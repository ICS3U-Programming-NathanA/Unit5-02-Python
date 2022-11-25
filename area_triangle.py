#!/usr/bin/env python3

# Created By: Nathan Araujo
# Date: Nov. 24, 2022
# This program calculates the area of a triangle in cm


def calc_area(base, height):

    # Calculates the area of the triangle
    area = (base * height) / 2

    # Rounds the area to 2 decimals
    area = round(area, 2)
    # Displays the area of the triangle
    print(f"The area of the triangle is {area}cm^2\n")


def main():

    # Asks the user to enter the base of the triangle
    base_str = input("Enter the base of the triangle in cm: ")
    # Asks the user to enter the height of the triangle
    height_str = input("Enter the height of the triangle in cm: ")
    # Try catch to catch if the user entered a string
    try:
        base = float(base_str)
        height = float(height_str)
    except:
        print("You must enter a valid integer.")
    else:
        # Calls the calc_area(base, height) function
        calc_area(base, height)


if __name__ == "__main__":
    main()
