# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def gather_user_name():
    """
    collect the name of the customer 
    """
    user_name = input("enter your name:\n")
    if user_name.isalpha():
        return user_name
    elif len(user_name) == 0:
        print("username is mandatory")
    else:
        print("invalid username")
        

def daily_steps():
    """
    collect the average number of daily steps
    """
    try:
        number_of_steps = int(input("Enter the average daily steps:\n"))
        if number_of_steps > 0:
            print(f"Hello {username}, your average daily steps are {number_of_steps}")
            return number_of_steps
        else:
            print("invalid number. try again")
    except ValueError:
        print("only numbers accepted.")
    #daily_steps = int(input("enter the average number of daily steps:\n"))
    #return user_name

#def kcal_burned():
    """
    define how many calories were burned so far
    Generally speaking, walking 10km will burn around 500-700 (i will use 600 
    as average of the 2 values)
    calories for an average person this function will use this for calculate
    the kcal already burnt
    """



print("Welcome to our StepCounter App\n")
print("This app was created for keep track of daily steps for weightloss\n")
print("Let's start!\n")

username = gather_user_name()
number_of_steps = daily_steps()