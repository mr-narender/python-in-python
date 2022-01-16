# Python in Python

## Important information for assessment team
When submitting to Heroku by following the steps [below](#deployment), after the receiving the message "Your app was successfully deployed". The "RUN PROGRAM" button returned this error message:
"pygame.error: No available video device".

This was the same error message that I received when first creating the game in GitPod. Hence, my decision to use Replit, another program recommended by Code Institute. They advised me to create an account when signing up to the course.

Below this section is a join link to the Replit file used to create and test the game. The GitHub repository containing the run.py file is an exact copy.

Unfortunately, I was never told that Pygame was incompatible with Heroku until the 15th January 2022 via a tutor support call [view log](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/tutor-assistance-call).
No concerns were ever mentioned in my mentor meetings throughout the project.

#

For the Replit join link, [click here.](https://replit.com/join/rpbaqgcglq-liamsmith3194)

Welcome to Python in Python. Based on the mobile game Snake. It was extremely popular when mobile phone had physical buttons rather than the modern touchscreens we see today. The aim of the game is to move the "snake" around the screen, collecting the "food" and not hitting the walls or crossing through yourself. Every time the food is collected, the snake grows, along with your score.

Screenshot of game here.

## User Experience (UX)

### First Time Visitor Goals

1. As a first time visitor, I want a clear understanding as to the objective of the game.
2. As a first time visitor, I want the controls to be as simple as possible.
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

![Features](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/snake-game.PNG)

### Chequered background

- The use of the dark chequered grid background makes the game more appealing than a boring black and white design. The snake and apple size matching the grid size (20px) shows a clear indication of where the snake and apple are and when to use the direction arrows on the keyboard.

### Growing snake

- This is a stereotypical feature of the game Snake and works in the exact same way. As the snake collects and eats the apple, the snake body increases by one square, making each level more and more challenging in terms of the player avoiding crashing into any part of the snake.

### Increasing speed

- The normal mobile features continue and not only does the snake increase in size but the speed of which the snake moves around the board increases too.

### Scoreboard

- When the snake has eaten the apple, the score increases by 10 points.

### Prints to the console

- Whilst playing the game, multiple print statements are used, including:
    - "Press any direction key to start the game." - This is displayed as the game loads and prompts the user to start using the correct keys.
    - "Unrecognised command." - This is printed if anything but an arrow key is used during the game.
    - "Well done! You ate the apple." - Prints every time the snake and apple position are an exact match.
    - "Game over! You hit the wall." - If the snake exceeds the screen width or height, it's game over and this is printed in the console.
    - "Game over! You hit yourself." - This is printed if the snake head is in contact with any part of the snake. This is also displayed if the snake reverses into its self (over 3 squares in length).
    - "Final score: ..." - At game over, the final score is printed to the console using the f-string of snake_score.

![Console prints](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/snake-game-console.PNG)

### Play again

- Eventually, when your turn is over, you have the option to play again or quit. If the user selects play again (Y) the score is reset to 0 and the snake size and speed is back to the default.

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
- [Heroku](https://www.Heroku.com/)
- Heroku was used to share the app online.
- [Lucidchart:](www.lucidchart.com)
- Lucidchart was used to create the step by step workflow to visualise the game.

## Testing

### Validation Testing

The [PEP8](http://pep8online.com/) Python linter was used to ensure there were no syntax errors in the project.
On the first use my code produced over 45 warnings and/or errors including:
- "blank line contains whitespace"
- "indentation is not a multiple of four"
- "line too long (93 > 79 characters)"


These have now all be rectified and the link to the results text document is below.
- [Final results](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/pep8-results.txt)

### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

Q1. As a first time visitor, I want a clear understanding as to the objective of the game.

- Since Snake was created in the late 90s, it has appeared on over 400 million mobile phones. There were no hesitation from the users playing this game.

Q2. As a first time visitor, I want the controls to be as simple as possible.

- It doesn't get much easier than up, down, left and right.

Q3. As a first time visitor, I want to have live scoring.

- The way the scoreboard is presented is easy to read even while concentrating on the game. The white makes it stands out from the grid and the Courier typeface give it a more game like feel rather than uses something standard like Arial for example.
- Keeping the score on the screen when the game is over is important, as it's not always possible to look at the score while playing the game, especially as the speed increases.

Q4. As a first time visitor, I want to enjoy the game and come back again and again.

- It's a classic game recreated and brought up to date. It was really addictive, just like the mobile version was years ago.

### Continued Testing

- Friends and family members were asked to review the game and documentation to point out any bugs and/or user experience issues.

### Glitches

- Gitpod and Heroku not displaying the game ("pygame.error: No available video device")
- End game message "\n" (new line) not working on display.

## Deployment

### Heroku

Heroku was the program used to share the game, it was accomplished by using the following steps:

1. Log in to Heroku. On your dashboard, click "New" and then click "Create new app".

2. Fill in the field for App name - It must be a unique name to Heroku. 
    -   Then select the region of Europe and click "Create app"

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/Heroku-new-app.PNG)

3. In the "Settings" tab, scroll down to "Buildpacks" and click "Add buildpack".
    -   Select "python" and click "Save changes"
    -   Select "node.js" and click "Save changes"

![Heroku - Add buildpack](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/Heroku-add-buildpack.PNG)

4. Scroll back and click the tab "Deploy"
    - Choose "GitHub" as the Deployment method
    - Enter the GitHub repository name and click "Search"
    - The repository should appear below, then click "Connect"

![Heroku - Deployment method](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/Heroku-deployment-method.PNG)

5. Then click the "Deploy Branch" button in the "Manual deploy" section. This way you can see the code being written.

![Heroku - Manual deployment](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/Heroku-manual-deploy.PNG)

6. Once that is complete, a message will appear with "Your app was successfully deployed" and a "View" button. This will take you to the app directly.

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/python-in-python/main/assets/readme-images/Heroku-deployed-successfully.PNG)

## References

### Code

- Title in Pygame window. [Stack Overflow](https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window)

- Chessboard grid [Stack Overflow](https://stackoverflow.com/questions/38083788/turn-grid-into-a-checkerboard-pattern-in-python)

- Pygame.rect - Draw rectangle [pygame.org](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect)

- Blit - Show score on grid [Stack Overflow](https://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever)

- Increasing snake length [CodeWithHarry](https://www.codewithharry.com/videos/python-game-development-17/)

### Content

- All content was written by the developer.

#### Import
- Pygame Module - "a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language." [pygame.org](https://www.pygame.org/wiki/about)

- Random Module - "The random module is a built-in module to generate the pseudo-random variables. It can be used to perform some action randomly such as to get a random number, selecting a random element from a list, shuffle elements randomly, etc." [Tutorials Teacher](https://www.tutorialsteacher.com/python/random-module)


### Mentions

- My Mentor for answering my questions throughout.

- Slack users for constructive feedback, suggestions for improvements and video calls.