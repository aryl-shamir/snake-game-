# 🐍 Snake Game in Python (Turtle Graphics)

This is a simple **Snake Game** built using Python's built-in **Turtle graphics** module. It recreates the classic snake arcade game where the player controls a snake that grows longer by eating food and loses the game upon hitting a wall or its own tail.

---

## 📁 Project Structure

```
snake-game/
├── main.py             # Main game loop and logic
├── snake.py            # Snake class: handles movement and growth
├── food.py             # Food class: manages food behavior and placement
├── scoreboard.py       # Scoreboard class: displays score and game-over
└── README.md           # Project documentation
```

---

## 🚀 How to Run the Game

### ✅ Requirements

- Python 3.x installed on your system (Turtle is included by default)

### ▶️ Steps

1. Clone this repository:

```bash
git clone https://github.com/aryl-shamir/snake-game.git
cd snake-game
```

2. Run the game:

```bash
python main.py
```

3. Control the snake using the **arrow keys** (`↑ ↓ ← →`).

---

## 🧠 Game Features and Development Steps

This game was built step-by-step following a TODO list:

### ✅ 1. Create a snake body

- The snake starts with 3 segments aligned horizontally, created using the `Turtle` class.

### ✅ 2. Make the snake move

- Each segment follows the one before it while the head keeps moving forward automatically.

### ✅ 3. Control the snake

- Use arrow keys to change direction:
  - `Up` → Move up
  - `Down` → Move down
  - `Right` → Move right
  - `Left` → Move left
- Direct reversal is blocked to prevent self-collision.

### ✅ 4. Detect collision with food

- If the snake's head comes within 15 pixels of the food, it:
  - Grows by one segment
  - Gains a point
  - The food relocates randomly on the screen

### ✅ 5. Create a scoreboard

- The score is displayed at the top.
- Score increases with each food eaten.
- Displays "Game Over" at the center when the game ends.

### ✅ 6. Detect collision with wall

- If the head hits the screen boundary (±290 in x or y), the game ends.

### ✅ 7. Detect collision with tail

- If the head touches any part of its body (tail), the game ends.

---

## 💡 Future Improvements

- Add sound effects on eating or game over
- Save and display high scores
- Increase speed as score increases
- Add obstacles or levels

---

## 👨‍💻 Author

**Your Name**  
GitHub: [@aryl-shamir](https://github.com/aryl-shamir)

---

## 🖼️ Optional: Add a Screenshot

You can add a screenshot of your game by replacing the placeholder below:

```markdown
![Snake Game Screenshot](screenshot.png)
```

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE) (add if you want).


