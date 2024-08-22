"""
CAPSTONE PROJECT I - finance_calculators.py:

Request the user to perform an investment or bond calculation

Investment - When selecting the investment option, the following must occur:
    - Request the user to enter amount of money being deposited (P)
    - Request the user to enter the interest rate (r)
    - Request the user to enter the number of years to invest (t)
    - Request the user to calculate their invest via simple or compound interest

    - If simple interest is selected, perform the following calculation:
          A = P(1 + r * t)

    - If compound interest is selected, perform the following calculation:
          A = P(1 + r)^t

    - Print the results of the investment calculation

Bond - When selcting the bond option, the following must occur:
    - Request the user to enter the present value of the house (P)
    - Request the user to enter the interest rate (i)
      i.e. i / 12 since it is in months
    - Request the user to enter the number of months to repay the bond (n)

    - Calculate the bond repayment using the following formula:
        repayment = (i * P)/(1 - (1 + i)**(-n))

    - Print the results of the bond calculation
"""
import math

# Using a while loop to continue the program to prevent invalid input from stopping the program.
while True:

    # Request user to select between the investment and bond options.
    user_option = input("Please select the follwoing options between: (array only)\n1. Investment \n2. Bond\n--->")

    print("---------------------------------------")

    # Request the user to enter the necessary information to calcuate their investment plan.
    if user_option == "1":

        P = float(input("Please enter the amount of money you wish to deposit: R"))
        r = float(input("Please enter the interest rate (excluding the '%' sign): ")) / 100
        t = int(input("Please enter the number of years you wish to invest: "))

        invest_option = input("Please select the follwoing options between: (array only)\n1. Simple Interest \n2. Compound Interest\n--->")

        print("--------")
        if invest_option == "1":
            A = P * (1 + r * t)
            print(f"Simple Interest Return: R{round(A, 2)}")

        elif invest_option == "2":
            A = P * math.pow((1 + r), t)
            print(f"Compound Interest Return: R{round(A, 2)}")

        else:
            print("Invalid entry! Please try again.")
        print("--------")

    # Request the user to enter the necessary information to calcuate their bond repayments.
    elif user_option == "2":
        P = float(input("Please enter the present value of your house: R"))
        i = float(input("Please enter the interest rate (excluding the '%' sign): ")) / 100 / 12
        n = int(input("Please enter the number of months you wish to repay your bond: "))

        repayment = (i * P) / (1 - (1 + i) ** (-n))

        print("--------")
        print(f"Bond Repayment per month: R{round(repayment, 2)}")
        print("--------")

    # Retry the progrma if invalid input is given
    else:
        print("Invalid Entry! Please try again.")

    # Request user to end the program or continue.
    end_program = input("Would you like to end the pragram?\n1. Yes\n(Enter any key). No---->")

    print("---------------------------------------")

    if end_program == "1":
        print("THANK YOU FOR USING THIS PROGRAM!")
        break
