
# overview
Welcome to my step counter app!

The purpose app is to motivate user to an healthy life: user can enter the steps and he can see live the average amount of calories burned so far.

[View my live project here](https://stepscounter-67b67669ecaa.herokuapp.com/)

## Features

### welcome message and a brief presentation of the app. 
in this screen, user is prompted to insert the name:

 ![welcome and first name](/media/Screenshot%202024-09-14%20000627.png)


### gather steps information
 user can now add the average number of daily steps:

![number of steps](/media/Screenshot%202024-09-14%20000720.png)


### outcome based on customer's data

- the first one if the user burned less than 50 kcal, and it is a motivational message:

![low calories burned](/media/Screenshot%202024-09-14%20004006.png)

the other one is shown if the user burned more than 50 kcal:

![high calorie burned](/media/Screenshot%202024-09-14%20000819.png)


## features to be added in future:

- in future it will be created a txt files with all the customer entries to keep track of the progress. this file will be shared in google, so it can be easy to be retrieved and shared at any time 
- add a function to restart the code if customer want to add more data.

## Technologies Used

- Python.
- [PEP8:](http://pep8online.com/) Check code for PEP8 requirements.
- [Git](https://git-scm.com/) to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/) the projects code was saved in github.
- [Heroku:](https://dashboard.heroku.com/) for deployment of the application.


## Testing

| ID | Test Label | Test | Test outcome |  
|----|---------------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|  1 | Welcome page Run program  | The user is presented with a welcome message and prompt to enter his name| PASS 
|  2 | enter a blank fields in name and number of steps     |  invalid input will result in a specific error message to the user. | PASS  | 
|  3 | enter a non strings value in name field|  invalid input will result in a specific error message to the user. | PASS  | 
|  4 | capitalize name | username is capitalized | PASS 
|  5 | enter a non integer number in number of steps| invalid input will result in a specific error message to the user. | PASS  | 
|  6 | expected outcome for number of steps and username in the messages | outcome is personalized as expected |PASS  
|  7 | different message shown based on kcal burned so far | different message is reported correctly |PASS 


### Validator results:

PEP8 Online (Python validator)
The code passed without any errors.

## known bug:

during pep8 validation, some lines were longer than 80. Using the backslash for fix this problem caused an unwanted space gap in gitpod:
![bug fouund in gitpod](/media/Screenshot%202024-09-14%20000836.png)