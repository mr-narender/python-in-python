# Python in Python

For the deployed website, [Click here.](https://liamsmith3194.github.io/python-in-python/)

Welcome to Python in Python. Based on the mobile game Snake. It was extremely popular when mobile phone had physical buttons rather than the modern touchscreens we see today. The aim of the game is to move the "snake" around the screen collecting the "food" and not hitting the walls or crossing through yourself.

Screenshot of game here.

## User Experience (UX)

### First Time Visitor Goals

1. As a first time visitor, I want a clear understand of the objective of game.
2. As a first time visitor, I want the controls to be as simple of possible.
3. As a first time visitor, I want to have live scoring.
4. As a first time visitor, I want to enjoy the game and come back again and again.

### Returning Visitor Goals

1. As a returning visitor, I want to enjoy the game as much as I did the first time.


### Design

- #### Colour Scheme
- The snake board is set on a dark chequered background #202937 - RGB (38,52,69) #263445 - RGB (32,41,55).
- #### Typography
- One typeface is used to show the scoreboard (Monotype). This is used as it brings an arcade like feel but is clear to read, especially when in white on the dark chequered background.


### Flowchart

- Lucidchart - [View](https://lucid.app/lucidchart/73191bed-4f56-4346-a1b2-0c396684c9c4/edit?invitationId=inv_35d8ac34-a4b0-41c5-a4f5-98f8ded0b418)

![Lucid Snake Flowchart](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/lucid-flowchart.PNG)


## Features
Below is a brief overview showing the main features of the game.

### Chequered background

- placeholder

### Growing snake

- placeholder

### Increasing speed

- placeholder

### Scoreboard

- placeholder

## Future Features

- placeholder

## Technologies

### Created by using:

- Python

### Programs including:

- [Replit](https://replit.com/)
- Replit was used instead of GitPod due to the functionality issue with the Pygame module. All coding and testing was created in Replit.
- [GitPod](https://gitpod.io/)
- GitPod was used via the terminal to push changes to GitHub.
- [GitHub:](https://github.com/)
- GitHub was used to embed the site and store all imagery.
- [Lucidchart:](www.lucidchart.com)
- Lucidchart was used to create the step by step workflow to visualise the game.

_____________________
ALL TO BE REPLACED BELOW


## Testing

### Validation Testing

The W3C Markup Validator and W3C CSS Validator Services were used to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fliamsmith3194.github.io%2Fpython-in-python%2F)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fliamsmith3194.github.io%2Fpython-in-python)
- [Jshint JavaScript linter](https://jshint.com/) - 26 warnings, the mast majority:
    -   'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    -   'template literal syntax' is only available in ES6 (use 'esversion: 6'.

### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

Q1. As a first time visitor, I want a clear understand of the objective of game.

- A large majority of the world's population have played or understand how Rock, Paper Scissors is played. As soon as users enter the site, it is abundantly clear what the game is and how to play it. The default icons on show increase the clarity.

Q2. As a first time visitor, I want the controls to be as simple of possible.

- The rules are very clear to see, labelled up beneath the interactive buttons. "ROCK BEATS SCISSORS" etc.

Q3. As a first time visitor, I want to have live scoring.

- Round by round after the alert message of the outcome, the round number is updated along with the tally of rounds won, rounds drawn or rounds lost, all looking from the user's perspective.

Q4. As a first time visitor, I want to enjoy the game and come back again and again.

- The way the game is run is so easy to play and understand. I have found myself saying "one more round" constantly, just to finish with a win and beat the computer.

### Continued Testing

- The Website was tested on Google Chrome, Internet Explorer (see glitches), Microsoft Edge and Safari browsers.
- The website has been displayed on various devices such as Desktop PC, iMac, Laptop, iPhone X & iPad Pro
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Glitches
#### Computers

- Internet Explorer - The website doesn't display any images or button labels. This leads to no functionality.

#### Mobile (iPhone X)
- The hover pseudo has been removed on smaller devices (tablet-phone) to ensure the user the game has been reset, as the button were not returning to original style after selection.
- The button images appear stretched. However, there were no issues via inspect mode in a browser.
- The button labels don't line up centrally beneath the buttons. Again, there were no issues via inspect mode in a browser.

## Deployment

### Heroku

GitHub was the program used to deploy the site, it was accomplished by using the following steps:

REPLACE !!!!

1. Log in to GitHub and select the GitHub Repository.

![GitHub Repository](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/github-repo.PNG)

2. At the top of the page towards the middle of the screen, you will see a "Settings" menu item with a cog icon.

![GitHub Settings](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/github-settings.PNG)
3. On the left-hand side is a vertical list, locate and click "Pages".

![GitHub Pages](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/github-pages.PNG)

4. Under the "Source" sub-heading, click on the dropdown by default "None" and choose "main".

![GitHub Source](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/github-source.PNG)

5. Click "Save"
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

![GitHub Publish](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/github-published.PNG)

## References

### Code

-   Title in Pygame window. [Stack Overflow](https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window)

-   Chessboard grid [Stack Overflow](https://stackoverflow.com/questions/38083788/turn-grid-into-a-checkerboard-pattern-in-python)

-   Pygame.rect [pygame.org](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect)

-   Blit - Show score on grid [Stack Overflow](https://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever)

-   Increasing snake length [CodeWithHarry](https://www.codewithharry.com/videos/python-game-development-17/)

### Content

#### Import
-   Pygame Module -  a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. [pygame.org](https://www.pygame.org/wiki/about)

-   Sys Module -   ajjkhbl

-   Random Module - sdffds [w3schools](https://www.w3schools.com/python/module_random.asp)


- All content was written by the developer.

### Mentions

- My Mentor for answering my questions throughout.

- Slack users for constructive feedback, suggestions for improvements and video calls.


________________________________



![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome liamsmith3194,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

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