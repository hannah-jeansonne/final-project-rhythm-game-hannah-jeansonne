# Final Project Proposal: Rhythm Game

## Repository
[Link to project repository](https://github.com/hannah-jeansonne/final-project-rhythm-game-hannah-jeansonne)

## Description
My project will be an interactive game where users have to press specified keys in time to the rhythm of a song. This relates to media and digital arts because it combines musical and graphic arts with digital media.

## Features
- Falling Key Indicators
	- Color coded particles move from the top to the bottom of the surface, deleting the particle when the correct key is pressed at the right time or the particle is off the screen.
- Music and Mapped Indicators
	- A music file will play during the level and the timing of the falling indicators will be mapped to the rhythm of the song.
- Visible Score
	- A counter adds a score for each indicator key hit within a small time frame of the beat. The score will be visible in the corner of the level.
- Start Menu
  - The surface that is displayed at the start of the program. It tells the player what to press to start the game.
- End Screen / Replay Button
  - At the end of the level, a new surface displays the final score and gives the player the option to play again.

## Challenges
- Adding music to programs in pygame.
- Timing particle movements to the beat of a music file.
- Specifying different key events to similar particles of a different color.
- Implementing the start and end screens.

## Outcomes
Ideal Outcome:
- A start menu that leads to a playable, fully mapped level of a rhythm game. In the level, there is visual graphic interface and color coded indicators for which keys to press and when. There is also a scoring system for the players accuracy, and the player can fail the level if they are too inaccurate. At the end, the player's score is displayed, and they are given the option to play again.

Minimal Viable Outcome:
- There is a playable level of a rhythm game that has color coded indicators to show the player which keys to press and when. There is a basic scoring system for the player's accuracy in timing the key presses.

## Milestones

- Week 1
  1. Add a song to the program
  2. Create falling particles in time with some beats of the song
  3. Make the particles interactive by changing the score when pressing any key when the particle reaches the designated point on the screen

- Week 2
  1. Specify different particle tracks/colors to different key events
  2. Finish mapping the song beats with falling particles

- Week 3
  1. Add start and end screen
  2. Finalize graphics to be more visually appealing
