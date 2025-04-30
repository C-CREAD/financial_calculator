"""
finance_calculator.py:

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

from flask import Flask, redirect, url_for, render_template, request

finance_app = Flask(__name__)


@finance_app.route("/")
@finance_app.route("/home")
def home_page():
    """This function renders the HTML template to
    load the financial calculator homepage."""

    return render_template("finance.html")


@finance_app.route("/investment", methods=["POST", "GET"])
def investment():
    """This function renders the HTML template to load the
    investment page and request the user to enter invest details.
    The backend will calculate the simple and compound interest
    returns. """

    import math

    if request.method == "POST":
        deposit = float(request.form["deposit"])
        interest_rate = float(request.form["interest"])/100
        period = int(request.form["period"])

        simple_interest = round(deposit * (1 + interest_rate * period), 2)
        compound_interest = round(deposit * math.pow((1 + interest_rate), period), 2)

        content = [deposit, interest_rate, period, simple_interest, compound_interest]

        return render_template("investment.html",
                               content=content)

    else:
        # Default content value is an empty list
        return render_template("investment.html", content=[])


@finance_app.route("/bond", methods=["POST", "GET"])
def bond():
    """This function renders the HTML template to load the
    investment page and request the user to enter invest details.
    The backend will calculate the simple and compound interest
    returns. """

    import math

    if request.method == "POST":
        present_value = float(request.form["present-value"])
        interest_rate = float(request.form["interest"])/100/12
        period = int(request.form["period"])

        repayment = round((interest_rate * present_value) / (1 - (1 + interest_rate) ** (-period)), 2)

        content = [present_value, interest_rate, period, repayment]

        return render_template("bond.html",
                               content=content)

    else:
        # Default content value is an empty list
        return render_template("bond.html", content=[])


if __name__ == "__main__":
    finance_app.run(debug=True)