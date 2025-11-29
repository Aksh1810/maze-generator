import pygame
import random

CELL_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GRAY = (180, 180, 180)

def generate_maze(rows, cols):
    maze = [[1] * cols for _ in range(rows)]

    def carve(x, y):
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < rows and 0 < ny < cols and maze[nx][ny] == 1:
                maze[nx - dx // 2][ny - dy // 2] = 0
                maze[nx][ny] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1, 1)

    # pick diagonal entry/exit
    if random.choice([True, False]):
        entry, exit_ = (1, 1), (rows - 2, cols - 2)
    else:
        entry, exit_ = (1, cols - 2), (rows - 2, 1)

    return maze, entry, exit_

def solve_maze(maze, entry, exit_):
    rows, cols = len(maze), len(maze[0])
    q = [(entry, [entry])]
    visited = set([entry])
    while q:
        (x, y), path = q.pop(0)
        if (x, y) == exit_:
            return path
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), path+[(nx, ny)]))
    return []

def draw(screen, maze, entry, exit_, path, solve_button):
    screen.fill(BLACK)
    rows, cols = len(maze), len(maze[0])
    for r in range(rows):
        for c in range(cols):
            color = WHITE if maze[r][c] == 0 else BLACK
            pygame.draw.rect(screen, color, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # entry/exit
    pygame.draw.rect(screen, GREEN, (entry[1]*CELL_SIZE, entry[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (exit_[1]*CELL_SIZE, exit_[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # path
    for (r, c) in path:
        pygame.draw.rect(screen, BLUE, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # button
    pygame.draw.rect(screen, GRAY, solve_button)
    font = pygame.font.SysFont(None, 30)
    txt = font.render("Solve", True, BLACK)
    screen.blit(txt, (solve_button.x+10, solve_button.y+10))

    pygame.display.flip()

# --- main ---
def main():
    pygame.init()

    # random size each run
    ROWS, COLS = random.choice([(21,21), (31,31), (41,41)])
    WIDTH, HEIGHT = COLS*CELL_SIZE, ROWS*CELL_SIZE + 50
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator & Solver")

    maze, entry, exit_ = generate_maze(ROWS, COLS)
    path = []
    solve_button = pygame.Rect(WIDTH//2 - 50, HEIGHT-40, 100, 30)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.collidepoint(event.pos):
                    path = solve_maze(maze, entry, exit_)

        draw(screen, maze, entry, exit_, path, solve_button)
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()