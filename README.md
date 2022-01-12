# Python in Python

For the deployed website, [Click here.](https://liamsmith3194.github.io/python-in-python/)

Welcome to Python in Python. Based on the mobile game Snake. It was extremely popular when mobile phone had physical buttons rather than the modern touchscreens we see today. The aim of the game is to move the "snake" around the screen collecting the "food" and not hitting the walls or crossing through yourself. Everytime the food is collected the snake grows, along with your score.

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
- A bright green is used to show the snake - #009f00 - RGB (0, 159, 0)
- A dark red is used to represent the apple - #c80000 - RGB (200, 0, 0)
- White is used to show the live score.
- Game over interface is a simple black screen and white text.
- #### Typography
- One typeface is used to show the scoreboard (Courier). This is used as it brings an arcade like feel but is clear to read, especially when in white on the dark chequered background.
- The "play again" message shown when the game is over is displayed in Helvetica.

![Design](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/start-game.PNG)

### Flowchart

- Lucidchart - [View](https://lucid.app/lucidchart/73191bed-4f56-4346-a1b2-0c396684c9c4/edit?invitationId=inv_35d8ac34-a4b0-41c5-a4f5-98f8ded0b418)

![Lucid Snake Flowchart](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/lucid-flowchart.PNG)

## Features
Below is a brief overview showing the main features of the game.

### Chequered background

- The use of the dark chequered grid background makes the game more appealing than a boring black and white design. The snake and apple size matching the grid size (20px) shows a clear indication of where the snake and apple are and when to use the direction arrows on the keyboard.

### Growing snake

- This is a sterotypical feature of the game and Snake and works in the exact same way. As the snake collects and eats the apple the snake body increases by one square making each level more and more challenging in terms of avoid crashing into any part of the snake.

### Increasing speed

- The normal mobile features continue and not only does the snake increase in size but the speed of which the snake moves around the board increases too.

### Scoreboard

- When the snake has eaten the apple the score increases by 10 points.

### Play again

- Eventually when your turn is over, you have the option to play again or quit. If the user selects play again (Y) the score is reset to 0 and the snake size and speed is back to the default.

![Features](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/snake-game.PNG)

## Future Features

- "Mirror walls" - Instead of the game ended when you hit any of the four walls, the snake would appear from the opposite wall and back into the grid. This was a feature that was created for Snake II.

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

The [PEP8](http://pep8online.com/) Python linter was used to ensure there were no syntax errors in the project.
On the first use my code produced over 45 warnings and/or errors including:
-   "blank line contains whitespace"
-   "indentation is not a multiple of four"
-   "line too long (93 > 79 characters)"

- [Final results](http://pep8online.com/)

### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

Q1. As a first time visitor, I want a clear understand of the objective of game.

- Since Snake was created in the late 90's it has appeared on over 400 million mobile phones. There were no hesitation from the users playing this game.

Q2. As a first time visitor, I want the controls to be as simple of possible.

- It doesn't get much easier than up, down, left and right.

Q3. As a first time visitor, I want to have live scoring.

- The way the scoreboard is presented is easy to read even while concentrating on the game. The white makes it stands out from the grid and the Courier typeface give it a more "gamey" feel rather than uses something standard like Arial for example.
- Keeping the score on the screen when the game is over is important as it's not alway possible to look at the score while playing the game especially as the speed increases.

Q4. As a first time visitor, I want to enjoy the game and come back again and again.

- It's a classic game recreated and brought up to date. It was really addictive just like the mobile version was years ago.

### Continued Testing

- Friends and family members were asked to review the game and documentation to point out any bugs and/or user experience issues.

### Glitches

-   End game message "\n" (new line) not working on display.

## Deployment

### Heroku

Heroku was the program used to deploy the site, it was accomplished by using the following steps:

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

- All content was written by the developer.

#### Import
-   Pygame Module -  "a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language." [pygame.org](https://www.pygame.org/wiki/about)

-   Random Module - "The random module is a built-in module to generate the pseudo-random variables. It can be used perform some action randomly such as to get a random number, selecting a random elements from a list, shuffle elements randomly, etc." [Tutorials Teacher](https://www.tutorialsteacher.com/python/random-module)


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