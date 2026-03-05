# Maze Generator & Solver

A Python application that randomly generates mazes and solves them using a visual GUI built with Pygame.

## Features

- **Random maze generation** using recursive backtracking (depth-first search)
- **Shortest-path solver** using breadth-first search (BFS)
- **Interactive GUI** — click the **Solve** button to visualize the solution
- **Randomized size** — each run creates a 21×21, 31×31, or 41×41 maze
- **Color-coded display**
  - ⬜ White — open passage
  - ⬛ Black — wall
  - 🟩 Green — entry point
  - 🟥 Red — exit point
  - 🟦 Blue — solution path

## Prerequisites

- Python 3
- [Pygame](https://www.pygame.org/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Aksh1810/maze-generator.git
cd maze-generator
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install pygame
```

### 4. Run the application

```bash
python main.py
```

A window will open displaying a randomly generated maze. Click the **Solve** button at the bottom of the window to find and display the shortest path from entry to exit.

## How It Works

### Maze Generation — Recursive Backtracking

The `generate_maze` function initializes a grid filled with walls, then carves passages by recursively visiting neighbors in random order, stepping two cells at a time to preserve wall structure.

### Maze Solving — Breadth-First Search

The `solve_maze` function uses BFS starting from the entry cell. It explores all four cardinal directions and returns the shortest path to the exit.

## Project Structure

```
maze-generator/
├── main.py        # Maze generation, solving, and GUI
├── .gitignore
└── README.md
```

## License

This project is provided as-is for educational purposes.
