import pygame
import random
import pygame.freetype

# Window dimensions
size_x = 400
size_y = 300

# Game state variables
is_Start = 0  # Indicates if the game has started
interval_time = 0  # Tracks game timer
count = 0  # Number of circles
circs = []  # List of circle objects
circ_size = 0  # Size of circles
best_time = [100 for i in range(10)]  # Best time records for each circle count
last_time = 0  # Time taken in the last round
answer = 0  # Player's input
pauseing = 0  # Pause state (0 = not paused, 1 = paused)
space_down = 0  # Tracks if the space key is pressed

dt = 0  # Delta time for frame-independent timing

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((size_x, size_y))  # Create game window
clock = pygame.time.Clock()  # Clock for managing frame rate
font = pygame.freetype.SysFont('Arial Black', 30)  # Font for rendering text

# Game loop control
running = True

while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            running = False

    # Keyboard input state
    keys = pygame.key.get_pressed()

    # Clear screen
    screen.fill("white")

    # Generate circles if game has not started
    if interval_time >= 0 and is_Start == 0:
        answer = 0  # Reset player's answer
        count = random.randint(1, 9)  # Randomize circle count
        circs = [{"x": 0, "y": 0} for _ in range(count)]  # Initialize circle list
        circ_size = random.randint(5, 30)  # Randomize circle size

        circ_id = 0
        while circ_id < count:
            possibility = True
            temp_circ = {
                "x": random.randint(size_x // 2 - circ_size * 4, size_x // 2 + circ_size * 4),
                "y": random.randint(size_y // 2 - circ_size * 4, size_y // 2 + circ_size * 4)
            }

            # Check if circle overlaps with existing ones
            for other_circ in circs:
                del_x = temp_circ["x"] - other_circ["x"]
                del_y = temp_circ["y"] - other_circ["y"]
                if del_x ** 2 + del_y ** 2 < (circ_size * 2) ** 2:
                    possibility = False
                    break

            if possibility:
                circs[circ_id] = temp_circ
                circ_id += 1

        is_Start = 1  # Mark game as started

    # Game in progress
    if interval_time >= 0 and is_Start == 1:
        screen.fill("white")

        # Show circles briefly
        if interval_time < 1 / 30:
            for circ in circs:
                pygame.draw.circle(screen, "black", (circ["x"], circ["y"]), circ_size)

        # Record player's answer
        for i in range(1, 10):
            if keys[getattr(pygame, f"K_{i}")]:
                answer = i

        # Evaluate answer
        if answer != 0:
            last_time = interval_time
            interval_time = -5  # Transition to feedback phase
            is_Start = 0

    # Feedback phase
    elif interval_time < 0:
        if keys[pygame.K_SPACE]:  # Pause/unpause toggle
            if space_down == 0:
                pauseing ^= 1
            space_down = 1
        else:
            space_down = 0

        # Display feedback
        if answer == count:
            if last_time <= best_time[count]:
                screen.fill("#800080")  # Best time
                best_time[count] = last_time
            elif last_time - best_time[count] < 0.5:
                screen.fill("#006400")  # Close to best time
            else:
                screen.fill("#B8860B")  # Correct but slower

            font.render_to(screen, (size_x // 2 - 55, size_y // 2 - 20), f"{last_time:.3f}", (255, 255, 255))
        else:
            screen.fill("#800000")  # Incorrect answer
            font.render_to(screen, (size_x // 2 - 55, size_y // 2 - 20), f"{count} -> {answer}", (255, 255, 255))

        # Show timer or pause state
        if pauseing == 0:
            font.render_to(screen, (size_x // 2 - 60, size_y // 2 + 20), f"{interval_time:.3f}", (255, 255, 255))
        else:
            font.render_to(screen, (size_x // 2 - 65, size_y // 2 + 20), "PAUSE", (255, 255, 255))

    # Update timer if not paused
    if pauseing == 0:
        interval_time += dt

    # Refresh display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    dt = clock.tick(60) / 1000

# Quit Pygame
pygame.quit()
