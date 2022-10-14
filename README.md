![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to my python readme for lovesandwiches,

This is the Code Institute student template for deploying my third portfolio project, the Python command-line project. 
The last update to this file was: **Oct 14, 2022**

The deployed version is here https://ib-sandwich.herokuapp.com/ 

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file using pip3 freeze and directing the output or copying to requirements.txt
* If not using our requirements.txt, you will need to `pip3 install gspread` to be able to import gspread to access your google sheet from the python code
* If not using our Heroku deployed environment, you will need your own creds.json to access your own google spreadsheet.
* Do not edit any of the other files or your code may not deploy properly

## Bugs fixed
* fixed pylint warnings about trailing spaces, space after # in comments, and e variable in except statment (had to make it a longer lower case variable name)
* also fixed pylint error if using space between print command and opening bracket i.e. print ("test") is incorrect - should be print("test") with no space.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
 
1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!