#Shoutout to SoloLearn, thanks for the awesome resource :)
#Inputs
# - First coefficient.
# - Second coefficient.
# - Third coefficient.
# - However many lines of x-values you would like to test. Remember to input 'x' when you're done!
#Input numbers into quadratic, then choose various x-values to test against the function.
def quadratic_calc():
    terms = ['first', 'second', 'third']
    coefficients = []
    x_values = []
    ans = []
    print("\n****** ax^2 * bx + c ******\n")
#Enter in a, b, c values, check for any invalid inputs.
    for t in terms:
        value_check = False
        while value_check is False:
            user_coef = input(f"Please enter the {t} coefficient:")
            try:
                coefficients.append(int(user_coef))
                value_check = True
            except ValueError:
                print("Sorry, the coefficient chosen is not a number. Try again.")
#Print function with provided inputs.
    print(f"\nHere is the funtion: {coefficients[0]}x^2 * {coefficients[1]}x * {coefficients[2]}\n")
    print("Next, enter the x values you would like to test. To exit, enter 'x'.")
    print("To see previously entered numbers, press 'c'.\n")
#Prompt for x-values, check for invalid inputs and if user chooses to leave program.
    exit = False
    while exit is False:
        user_x_value = input("Enter an x-value: ")
        if user_x_value == 'x':
            if len(x_values) == 0:
                print("No x-values entered. Now exiting..")
                break
            elif len(x_values) == 1:
                print(f"Done, {len(x_values)} x-value entered.")
                exit = True
            elif len(x_values) > 0:
                print(f"Done, {len(x_values)} x-values entered.")
                exit = True
        elif user_x_value == 'c':
            if len(x_values) == 0:
                print("\nYou currently have no items in your list.\n")
            else:
                print(f"\n{x_values}\n")
        else:
            try:
                x_values.append(int(user_x_value))
                print(f"{user_x_value} will be tested.")
            except ValueError:
                print("Sorry, that value is not accepted. Please try again.")
#Calculates and prints results for each provided x-value.
        if exit is True:
            print(f"The following x-values were tested: {x_values}")
            for x in x_values:
                calc = coefficients[0]*x**2 + coefficients[1]*x + coefficients[2]
                ans.append(calc)
            print(f"The following are the answers: {ans}")
    print("Thank you.")

quadratic_calc()