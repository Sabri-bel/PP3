
# overview

Welcome to my step counter app!

The purpose of this app is to motivate user to an healthy lifestile: user can enter the steps and see the average amount of calories burned so far.

[View my live project here](https://stepscounter-67b67669ecaa.herokuapp.com/)

## Features

### welcome message and a brief presentation of the app. 

In this screen, user is prompted to insert his name:

 ![welcome and first name](/media/Screenshot%202024-09-14%20000627.png)


### gather steps information

User can now add the average number of daily steps:

![number of steps](/media/Screenshot%202024-09-14%20000720.png)


### outcome based on customer's data

- the first outcome is related to the user that burned less than 50 kcal, and this is a motivational message:

![low calories burned](/media/Screenshot%202024-09-14%20004006.png)

- the second outcome is shown if the user burned more than 50 kcal:

![high calorie burned](/media/Screenshot%202024-09-14%20000819.png)


## features to be added in future:

- Create a txt files with all the customer entries to keep track of the progress. this file will be shared in google, so it can be easily retrieved and shared at any time.
- Add a function to restart the code if the customer want to add more data.

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

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

  - Log in to GitHub and locate the GitHub Repository
  - At the top of the Repository, locate the "Settings" Button on the menu.
  - Scroll down the Settings page until you find the "Pages" Section.
  - from "Source" select "Master Branch", The page will automatically refresh.
  - scroll down through the page to locate in the right side the link in the deployments section under "GitHub Pages".


### Steps to deploy site using Heroku:

- On the Heroku dashboard, select "New" and click "Create new app"
  - insert the app name (it must be unique)
  - Select the location (US or Europe)
  - Click "Create app"
- locate the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - Add key "PORT" and value "8000" as config var
  - Click "Add"
  - Scroll down to Buildpacks and click "Add buildpack"
  - Add "python" as buildpack and click "Save changes"
  - Then, select "node.js" as second buildpack and click "Save changes" again
- Go to the Deploy tab:
  - Select GitHub and confirm the connection with the GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options and Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository; or in manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"


### Steps to clone site:

- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.

## Credits:

- all content was written by the developer