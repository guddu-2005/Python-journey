import tkinter as tk
import random
import time

# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
WINDOW_TITLE   = "🐍 Snake Game"
CANVAS_WIDTH   = 600
CANVAS_HEIGHT  = 600
CELL_SIZE      = 20        # pixels per grid cell
GRID_W         = CANVAS_WIDTH  // CELL_SIZE   # 30 columns
GRID_H         = CANVAS_HEIGHT // CELL_SIZE   # 30 rows

INITIAL_SPEED  = 130       # milliseconds between frames (lower = faster)
SPEED_INCREASE = 3         # ms reduction per food eaten
MIN_SPEED      = 60        # fastest possible speed

# Colours
BG_COLOR       = "#0d1117"
GRID_COLOR     = "#161b22"
SNAKE_HEAD     = "#39d353"
SNAKE_BODY     = "#26a641"
SNAKE_OUTLINE  = "#1a7f37"
FOOD_COLOR     = "#f85149"
FOOD_OUTLINE   = "#b91c1c"
TEXT_COLOR     = "#e6edf3"
SCORE_COLOR    = "#58a6ff"
GAMEOVER_BG    = "#21262d"


# ─────────────────────────────────────────────
#  SNAKE GAME CLASS
# ─────────────────────────────────────────────
class SnakeGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.high_score = 0
        self._build_ui()
        self._bind_keys()
        self.reset_game()

    # ── UI Construction ──────────────────────
    def _build_ui(self):
        # Header bar
        header = tk.Frame(self.root, bg=BG_COLOR)
        header.pack(fill="x", padx=16, pady=(12, 4))

        tk.Label(header, text="🐍 SNAKE", font=("Consolas", 18, "bold"),
                 bg=BG_COLOR, fg=SNAKE_HEAD).pack(side="left")

        self.score_var = tk.StringVar(value="Score: 0")
        self.hi_var    = tk.StringVar(value="Best: 0")

        tk.Label(header, textvariable=self.hi_var,
                 font=("Consolas", 12), bg=BG_COLOR, fg="#8b949e").pack(side="right", padx=8)
        tk.Label(header, textvariable=self.score_var,
                 font=("Consolas", 12, "bold"), bg=BG_COLOR, fg=SCORE_COLOR).pack(side="right", padx=8)

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
            bg=BG_COLOR, highlightthickness=2,
            highlightbackground=SNAKE_BODY
        )
        self.canvas.pack(padx=16, pady=(4, 4))

        # Footer
        footer = tk.Frame(self.root, bg=BG_COLOR)
        footer.pack(fill="x", padx=16, pady=(0, 10))
        tk.Label(footer, text="Arrow Keys / WASD  •  P to Pause  •  R to Restart",
                 font=("Consolas", 9), bg=BG_COLOR, fg="#484f58").pack()

    def _bind_keys(self):
        self.root.bind("<KeyPress>", self._on_key)

    # ── Game State ───────────────────────────
    def reset_game(self):
        self.snake      = [(GRID_W // 2, GRID_H // 2)]   # list of (col, row)
        self.direction  = (1, 0)   # moving right
        self.next_dir   = (1, 0)
        self.score      = 0
        self.speed      = INITIAL_SPEED
        self.running    = True
        self.paused     = False
        self.game_over  = False

        self._place_food()
        self._draw()
        self._tick()

    def _place_food(self):
        while True:
            pos = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
            if pos not in self.snake:
                self.food = pos
                break

    # ── Main Loop ────────────────────────────
    def _tick(self):
        if not self.running:
            return
        if self.paused:
            self.root.after(100, self._tick)
            return

        self._move()
        self._draw()

        if not self.game_over:
            self.root.after(self.speed, self._tick)

    def _move(self):
        self.direction = self.next_dir
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_W, (head_y + dy) % GRID_H)

        # Collision: hit self
        if new_head in self.snake:
            self._trigger_game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            # Ate food
            self.score += 10
            self.speed = max(MIN_SPEED, self.speed - SPEED_INCREASE)
            self.score_var.set(f"Score: {self.score}")
            if self.score > self.high_score:
                self.high_score = self.score
                self.hi_var.set(f"Best: {self.high_score}")
            self._place_food()
        else:
            self.snake.pop()   # remove tail

    def _trigger_game_over(self):
        self.game_over = True
        self.running   = False
        self._draw_game_over()

    # ── Rendering ────────────────────────────
    def _draw(self):
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_food()
        self._draw_snake()
        if self.paused:
            self._draw_pause()

    def _draw_grid(self):
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            self.canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill=GRID_COLOR)
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            self.canvas.create_line(0, y, CANVAS_WIDTH, y, fill=GRID_COLOR)

    def _draw_snake(self):
        for i, (col, row) in enumerate(self.snake):
            x1 = col * CELL_SIZE + 2
            y1 = row * CELL_SIZE + 2
            x2 = x1 + CELL_SIZE - 4
            y2 = y1 + CELL_SIZE - 4
            color   = SNAKE_HEAD if i == 0 else SNAKE_BODY
            radius  = 5 if i == 0 else 3
            self._rounded_rect(x1, y1, x2, y2, radius, fill=color, outline=SNAKE_OUTLINE, width=1)

            # Eyes on the head
            if i == 0:
                dx, dy = self.direction
                ex, ey = (x1 + x2) // 2, (y1 + y2) // 2
                offsets = [(-3, -3), (3, -3)] if dy == 0 else [(-3, -3), (-3, 3)]
                for ox, oy in offsets:
                    self.canvas.create_oval(
                        ex + ox - 2, ey + oy - 2,
                        ex + ox + 2, ey + oy + 2,
                        fill="white", outline=""
                    )

    def _draw_food(self):
        col, row = self.food
        x1 = col * CELL_SIZE + 3
        y1 = row * CELL_SIZE + 3
        x2 = x1 + CELL_SIZE - 6
        y2 = y1 + CELL_SIZE - 6
        self.canvas.create_oval(x1, y1, x2, y2,
                                fill=FOOD_COLOR, outline=FOOD_OUTLINE, width=2)
        # Shine dot
        self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 6, y1 + 6,
                                fill="#fca5a5", outline="")

    def _draw_pause(self):
        self.canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT,
                                     fill="#0d111788", stipple="gray50")
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                                text="⏸  PAUSED", font=("Consolas", 28, "bold"),
                                fill=TEXT_COLOR)
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 40,
                                text="Press P to continue", font=("Consolas", 13),
                                fill="#8b949e")

    def _draw_game_over(self):
        # Dim overlay
        self.canvas.create_rectangle(80, CANVAS_HEIGHT // 2 - 110,
                                     CANVAS_WIDTH - 80, CANVAS_HEIGHT // 2 + 110,
                                     fill=GAMEOVER_BG, outline="#30363d", width=2)
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 70,
                                text="GAME OVER", font=("Consolas", 30, "bold"),
                                fill=FOOD_COLOR)
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 20,
                                text=f"Score:  {self.score}",
                                font=("Consolas", 16), fill=SCORE_COLOR)
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 15,
                                text=f"Best:   {self.high_score}",
                                font=("Consolas", 16), fill=TEXT_COLOR)
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 65,
                                text="Press  R  to play again",
                                font=("Consolas", 13), fill="#8b949e")

    def _rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        """Draw a rectangle with rounded corners on the canvas."""
        pts = [
            x1 + r, y1,
            x2 - r, y1,
            x2,     y1,
            x2,     y1 + r,
            x2,     y2 - r,
            x2,     y2,
            x2 - r, y2,
            x1 + r, y2,
            x1,     y2,
            x1,     y2 - r,
            x1,     y1 + r,
            x1,     y1,
        ]
        self.canvas.create_polygon(pts, smooth=True, **kwargs)

    # ── Input Handling ───────────────────────
    def _on_key(self, event):
        key = event.keysym.lower()

        direction_map = {
            "up":    (0, -1), "w": (0, -1),
            "down":  (0,  1), "s": (0,  1),
            "left":  (-1, 0), "a": (-1, 0),
            "right": (1,  0), "d": (1,  0),
        }

        if key == "r":
            self.running = False          # stop any pending tick
            self.root.after(50, self.reset_game)
            return

        if key == "p":
            if not self.game_over:
                self.paused = not self.paused
                if not self.paused:
                    self._tick()
                else:
                    self._draw()
            return

        if key in direction_map and not self.game_over and not self.paused:
            new_dir = direction_map[key]
            # Prevent reversing into self
            if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
                self.next_dir = new_dir


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
