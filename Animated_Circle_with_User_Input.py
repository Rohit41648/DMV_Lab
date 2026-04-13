import pygame
import sys

# ================================
# 1. User Input
# ================================
width = int(input("Enter window width: "))
height = int(input("Enter window height: "))
speed = int(input("Enter circle speed: "))

# ================================
# 2. Initialize Pygame
# ================================
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties
x, y = width // 2, height // 2
radius = 30

# Direction of movement
dx, dy = speed, speed

clock = pygame.time.Clock()

# ================================
# 3. Animation Loop
# ================================
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move circle
    x += dx
    y += dy

    # Bounce from walls
    if x - radius <= 0 or x + radius >= width:
        dx = -dx
    if y - radius <= 0 or y + radius >= height:
        dy = -dy

    # Draw circle
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.update()
    clock.tick(60)