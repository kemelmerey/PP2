import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Red Ball')

ball_x = 400
ball_y = 300
ball_radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball_y -= 20
    if keys[pygame.K_DOWN]:
        ball_y += 20
    if keys[pygame.K_LEFT]:
        ball_x -= 20
    if keys[pygame.K_RIGHT]:
        ball_x += 20

    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    if ball_x + ball_radius > screen.get_width():
        ball_x = screen.get_width() - ball_radius
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
    if ball_y + ball_radius > screen.get_height():
        ball_y = screen.get_height() - ball_radius

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    pygame.display.update()