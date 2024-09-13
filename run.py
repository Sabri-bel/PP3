# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def gather_user_name():
    """
    collect the name of the customer as variable and
    add validation steps for avoid accidental insertion of number
    add valildation also for none value
    """

    while True:
        try:
            user_name = input("enter your first name:\n")
            if user_name.isalpha():
                return user_name.capitalize()
            elif len(user_name) == 0:
                print("Ouch! Username is mandatory\n")
            else:
                print("Invalid username. Insert your first name only\n")
        except ValueError:
            print("Please try again")


def daily_steps(username):
    """
    collect the average number of daily steps
    add validation for numbers only
    """

    while True:
        try:
            number_of_steps = int(input(
                "Enter the average number of your daily steps:\n"))
            if number_of_steps > 0:
                print(
                    f"you entered {number_of_steps} steps.\n")
                return number_of_steps
            else:
                print("invalid number. try again\n")
        except ValueError:
            print("only numbers accepted.\n")


def kcal_burned(username, number_of_steps):
    """
    define how many calories were burned so far
    Generally speaking, walking 10km will burn around 500-700 (i will use 600
    as average of the 2 values)
    calories for an average person this function will use this for calculate
    the kcal already burnt
    calory rounded to the integer (no decimal number)
    """

    single_step = 600 / 10000  # 600 kcal average for 10k km, single step calculated
    daily_kcal_burned = round(number_of_steps * single_step)

    if daily_kcal_burned > 50:
        print(f"Great news {username}, you already burned {daily_kcal_burned} \
              Kcal today! keep going!\n")
    else:
        print(f"{username}, you burned {daily_kcal_burned} kcal so far, \
              but you can do better!\n")


print("Welcome to our StepCounter App\n")
print("This app was created for keep track of daily steps for weightloss\n")
print("Let's start!\n")


def main():
    """
    main function that run all the program function
    """

    username = gather_user_name()
    number_of_steps = daily_steps(username)
    daily_kcal_burned = kcal_burned(username, number_of_steps)


main()
