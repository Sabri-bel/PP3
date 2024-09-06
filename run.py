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
    number_of_steps = int(input("Enter the average daily steps:\n"))
    print(number_of_steps)
    #daily_steps = int(input("enter the average number of daily steps:\n"))
    #return user_name


print("Welcome to our StepCounter App\n")
print("This app was created for keep track of daily steps for weightloss\n")
print("Let's start!\n")

gather_user_name()
daily_steps()