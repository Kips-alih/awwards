# The MoAwwards2021

## By [Alphonce Kipngeno](https://github.com/Kips-alih) ,December 2021

## Description

The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## Setup/InstallationDate posted: Instructions

### To get the project into your local machine

* Open your terminal
* Create a folder and navigate to the folder you created.
* Run `https://github.com/Kips-alih/awwards.git`
* Run `cd awwards` command to confirm it was successfully cloned.
* Run `virtualenv virtual`to create a virtual environment and activate by running `source virtual/bin/activate`

* Run `pip install -r requirements.txt` to Install the requirements.

### Testing the application

* Setup the database name,user, password and host.
* Make migrations using the command `Python manage.py makemigrations`
* Then migrate the changes using the command `Python manage.py migrate`
* Then test the application by running the command `Python manage.py test`

### Running the application

* Run `Python manage.py runserver`

## User Stories

Here are some user stories:

* Sign up and login to the application.
* Post and review Projects in the application.
* View a project through a live link.
* Search for different projects by their titles.
* View my projects on the profile page.

## Technologies used

* Python3.8
* Django2.2.4

## Support and contact details

Reach out to me through the following email addresses:

* alphonce.kipngeno@student.moringaschool.com.
* alphoncekipngeno@gmail.com.

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
