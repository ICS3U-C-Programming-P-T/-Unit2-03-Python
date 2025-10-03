#!/usr/bin/env python3
# Created By: Patrick
# Date: 9/30/2025
# Asks user for the diameter of
# pizza then caluclates and displays the full cost of pizza plus tax
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = +constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.INGRED_COST * subtotal
    total = subtotal * tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
