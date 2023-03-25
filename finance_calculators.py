# calling the built-in module math which extends the number of math
# functions you can use
import math

# introductory printed statements, setting out some initial options for the
# user
print("Choose either 'investment' or 'bond' from the menu below to proceed: "
      "\n")
print("investment - to calculate the amount of interest you'll earn on your "
      "investment")
print("bond       - to calculate the amount you'll have to pay on a home "
      "loan\n")

# A number of if statements nested within a while loop, ask the user for
# their choice, if it's not recognised print the error message and start the
# while loop again until input is recognised. Once the choice is made the
# statement gathers more inputs and calculates the answer, then breaks out
# of the loop.
while True:

    # this along with the else statement at the bottom will continually
    # print until one of the if/elif statements run
    invest_type = input("Please enter your choice: ")

    # if user chooses investment ask if they want simple or compound and
    # print answer
    if invest_type.lower() == "investment":
        money = int(input("How much money will you deposit? Please only "
                          "enter integers: "))
        interest_rate = int(input("Enter the interest rate as a percentage, "
                                  "Please only enter integers: "))
        num_years = int(input("How many years do you plan on investing for? "))
        interest_type = input("Do you want Simple or Compound interest? ")
        r = interest_rate / 100

        # if user chose simple interest, use equation to calculate the cost
        # and print
        if interest_type.lower() == "simple":
            total_amount_simple = money * (1 + r * num_years)
            print(f"If you invest £{money} over {num_years} years with an "
                  f"{interest_rate}% interest rate you will have "
                  f"£{round(total_amount_simple, 2)}.")
            break

        # else if the user chose compound interest, use a different equation
        # to calculate the cost and print
        elif interest_type.casefold() == "compound":
            total_amount_compound = money * math.pow((1 + r), num_years)
            print(f"If you invest £{money} over {num_years} years with an "
                  f"{interest_rate}% interest rate you will have "
                  f"£{round(total_amount_compound, 2)}.")
            break

    # else if user chooses bond use bond equation and print monthly repayments
    elif invest_type.casefold() == "bond":
        house_value = int(input("How much is your house currently worth? "))
        bond_interest = int(input("Enter the interest rate as a percentage, "
                                  "Please only enter integers: "))
        num_months = int(input("How many months do you need to repay the "
                               "bond? "))
        annual_interest = bond_interest / 100
        bond_repay = (annual_interest / 12) * \
                     (1 / (1 - (1 + annual_interest / 12) ** (
                         -num_months))) * house_value
        print(
            f"If your house is worth £{house_value} and the interest rate is "
            f"{bond_interest}% it will cost you £{round(bond_repay, 2)} per "
            f"month for {num_months} months to repay the bond.")
        break

    # else user inputs anything else print error message and return to while
    # loop until a break condition is met
    else:
        print("That is not an option, please try again.")
