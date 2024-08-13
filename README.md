# Python Programming MOOC 2024 - University of Helsinki

# Space Invaders

This is a simple "Space Invaders"-style game developed in Python using the Pygame library. The objective of the game is to control a robot, avoid falling monsters, and survive as long as possible. The game ends when the robot's health drops to zero.

## Game Description

In this game, you control a robot that can move left, right, up, and down to avoid falling monsters. Each time a monster collides with the robot, you lose some health points. The game becomes progressively harder as the speed and frequency of falling monsters increase over time. The game ends when your health reaches zero.

## Features

- **Dynamic Difficulty**: The speed of the falling monsters and their spawn rate increases over time.
- **Health and Score Tracking**: The game tracks the player's health and score in real-time.
- **Simple Controls**: Use the arrow keys to move the robot and avoid collisions.

## Installation

To run this game, you need to have Python installed along with the Pygame library. You can install Pygame using pip:

```bash
pip install pygame
```

## How to Run the Game

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/space-invaders.git
   ```

2. Navigate to the project directory:

   ```bash
   cd space-invaders
   ```

3. Run the game script:

   ```bash
   python game.py
   ```

## Controls

- **Arrow Keys**: Move the robot left, right, up, and down.

## Game Mechanics

- **Collision Detection**: The game checks for collisions between the robot and falling monsters. If a collision is detected, the player loses health points.
- **Score System**: The score increases over time as you survive longer.
- **Health**: The player starts with a health value of 50. Each collision reduces health, and the game ends when health drops below zero.

## Future Improvements

- Add sound effects and background music.
- Introduce power-ups to regain health or slow down monsters.


## Acknowledgments

This project was developed as part of the Python Programming MOOC 2024 by the University of Helsinki.

---

Make sure to replace `yourusername` with your actual GitHub username and adjust the paths or instructions according to your project setup. Save this content into a file named `README.md` in your project's root directory. This will be automatically displayed on your GitHub repository page.
