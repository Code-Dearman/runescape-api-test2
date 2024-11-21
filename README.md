_# Runescape data 
To find data attatch /player-stats/< player-name >/ to the end of the server url._

# RuneTask

RuneTask is a simple, users-friendly to-do list web app built with Django. Users can create, manage and track their goals with the option to link their current runescape character details in order to keep track of their goals. This project was created as part of my Code Institute 16 week bootcamp course. The aim is to use the Django framework to create a full-stack project which is hosted on Heroku. There must be a custom database table and the app must provide some CRUD functionality.

_img_

Live site: _link_

Admin access link: _link_

GitHub repository: _link_

## Table of Contents

1. [RuneTask Introduction](#RuneTask)
2. [How To Use The App](#how-to-use-the-app)
3. [UX - User Experience](#ux---user-experience)
4. [Project Planning](#project-planning)
    - [Agile](#agile)
    - [Wireframe](#wiresframes)
    - [MosCoW](#moscow)
    - [User Stories](#user-stories)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
5. [Security](#security)
6. [Features](#features)
7. [Future Features](#future-features)
8. [Technology and Languages](#technology-and-languges)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Tools and Programs](#tools-and-programs)
9. [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [User Testing](#user-testing)
    - [Automated Testing](#automated-testing)
10. [Deployment](#deployment)
    - [GitHub](#github)
    - [Django](#django)
    - [Cloudinary](#cloudinary)
    - [PostgreSQL](#postgresql)
    - [Heroku](#heroku)
    - [Clone](#clone)
    - [Fork](#fork)
11. [Credits](#credits)


## How to use the app

Using the app is simple! Unregistered users can stay on the homepage to view tasks which registered users have made public. However, to start working with the app you must register. 

Click the 'Sign Up' link in the navigation bar to create and account. Once this step is complete you can start making lists. Navigate to the 'Profile' link and press the 'New Task' button. Here you can specify what skill you are planning to train, outline what steps you must take (using the rich text editor) and choose whether to make the list public or keep it private.

For even greater functionality you can use the 'link character' button feature to safely use runescape's own Oldschool Hiscrores API to retrieve details about your character. Doing this allows your profile to display your current stats which you can incorporate into the task list. 

If you feel like customising you profile feel free to choose from a range of provided profile images.

When you've completed your task you can edit the task list and mark it as complete. Feel free to upload a screenshot of your success!

## UX - User Experience

_Description of how I decided on the colour palettes and why I made certain choices. Discuss the accessibility and responsiveness of the app._

## Project Planning

### Agile

This project was created using the agile methodology, particularly in relation to creating granular user stories which streamlines the development process. All of these user stories were gathered into a project kanban board on GitHub where I could pull stories from the backlog to the in progress column. Once I had completed the tasks they were moved into the completed column.  

_img of project board_

### User Stories

_All user stories marked with could should might and wont_

### MoSCoW

All of the user stories I created were sorted using the MoSCoW (Must have, Should Have, Could Have and Wont Have) prioritisation system. This system allowed me to organise my userstories, making sure that all the must haves formed my minimum viable product. Once those were completed I could advance towards including my Should and Could have user stories which would provide extra features for the user and lead to a more finished product. My wont have stories outlines features which were not in the scope of this development cycle but helped me to keep a focus on where the project is leading.

_MoSCow examples images_

### Wiresframes

The wire framing for this project was done using the free trial of [wireframe.cc](#https://wireframe.cc/). 

_Wire framing images_

### Entity Relationship Diagram

The entity relationship diagram for this project was created using [SmartDraw](#https://www.smartdraw.com/)

_ERD images_

## Security

Fortunately Django contains a lot of inbuilt security features such as CSRF protection, the encrypted storage of passwords and the ability to create a superuser to manage and control what data is entered into the public site. 

This last point was particulary importand for my project as I have a public area where users can post their to-do lists to the home page. The superuser abilites mean that I am able to approve or deny public lists before they are posted to the homepage and thus ensure that there is no sensitive or offensive content. 

## Features

Users can:
- View public lists on the homepage
- Create an account
- Login to their account
- Create a new to-do list
- View their to-do lists
- Request their list to be made public
- Link their runescape character to their profile
- Delete their to-do lists
- Mark their to-do lists as completed

_img of various features_

Superusers can:
- View all public lists
- Approve public list requests
- Create and delete lists

## Future Features

_Outline future features_

## Technology and Languges

### Languages

The languages used for this project were:
- HTML
- CSS
- JavaScript
- Python

### Frameworks

The frameworks used for this project were:
- Django
- Bootstrap

### Tools and Programs

Additional tools and programs used include:
- wireframe.cc for wireframe creation
- SmartDraw for ERD
- chatGPT for general advice and insight on project planning, error checking code snippets and spell checking.
- FontAwesome for webpage icons
- Googlefonts for fonts
- Git for version control
- Gitpod for writing and pushing code to repository. 
- GitHub for storing repository

## Testing

### Validation Testing

The validation testing was done using the [W3C](#https://www.w3.org/) website HTML and CSS validator.

_add images of complete validation testing_

### User Testing

Manual user testing was done by me. I made sure that I could access and perform all the neccessary features, both as user and superuser. This included:
- Making to-do lists (as user and superuser)
- Deleting to-do lists (as user and superuser)
- Requesting lists be made public (as user)
- Approving lists (as superuser)
- Linking runescape characters (as user)
- Creating new accounts (as user)

**Browser Compatablity**: The website was tested Firefox and Chrome for desktop view and Safari and Firefox for mobile view.

**Responsiveness Testing**: I tested the responsiveness of all areas of the website on both desktop and mobile phone views.

### Automated Testing

_Write about automated tests or delete if unable to complete in time_

## Deployment

### GitHub

This project was created on the Gitpod CDE and Git was used for version control. The repository is stored on GitHub and was linked to Heroku for deployment.

### Django

Django was essential to the deployment process as it works seemlessly with Heroku. Adding allowed hosts in config/settings.py means that you can choose what hosts are allowed for the website. 

### Cloudinary

_Add cloudinary info later_

### PostgreSQL

_add later_

### Heroku

Deploying on Heroku was done with these steps.

- Create a new Heroku app.
- Choose GitHub as the deployment method in the app dashboard.
- For my project I did manual deployments from the main branch.
- Set the config vars in Heroku to match the vars in eny.py to protect secret keys and passwords.
- Click deploy and wait for Heroku to finishing setting up the website.

### Clone 



### Fork



## Credits