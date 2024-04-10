# Import the pygame library for building games
import pygame
# Import the random module for generating random numbers
import random

# Initialize pygame
pygame.init()

# Define some color constants using RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set the width and height of the display window
dis_width = 800
dis_height = 600
# Create a display surface with the specified dimensions
dis = pygame.display.set_mode((dis_width, dis_height))
# Set the caption of the display window
pygame.display.set_caption('Snake Game')

# Create a Clock object to control the frame rate of the game
clock = pygame.time.Clock()

# Define the size of the snake block and the speed of the snake
snake_block = 10
snake_speed = 15

# Define font styles for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score and level
def Your_score(score, level):
   # Render the score and level text
   value = score_font.render("Your score: " + str(score) + " and Your level: " + str(level), True, WHITE)
   # Draw the text on the display surface
   dis.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
   # Iterate over each segment of the snake and draw a rectangle for each segment
   for x in snake_list:
       pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color):
   # Render the message text
   mesg = font_style.render(msg, True, color)
   # Draw the text on the display surface
   dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to start the game loop
def gameLoop():
   # Make some variables global
   global snake_speed
   # Set initial game states
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   snake_List = []
   Length_of_snake = 1
   level = 1
   # Generate initial position for food
   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
   
   # Main game loop
   while not game_over:
       # Handle events
       while game_close == True:
           # Display message when game is over
           dis.fill(BLACK)
           message("Game Over! Press Q for exit or press C to play again!", RED)
           # Display score and level
           Your_score(Length_of_snake - 1, level)
           # Update the display
           pygame.display.update()
           # Check for events
           for event in pygame.event.get():
               # Check if the user wants to quit or play again
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       gameLoop()
       
       # Handle keyboard events
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP or event.key == pygame.K_w:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                   y1_change = snake_block
                   x1_change = 0
       
       # Check if the snake hits the boundaries
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
       
       # Move the snake
       x1 += x1_change
       y1 += y1_change
       # Clear the display
       dis.fill(BLACK)
       # Draw the food
       pygame.draw.rect(dis, RED, [foodx, foody, snake_block, snake_block])
       # Create a list to represent the snake's head
       snake_Head = []
       snake_Head.append(x1)
       snake_Head.append(y1)
       # Add the snake's head to the snake list
       snake_List.append(snake_Head)
       
       # Check if the snake has collided with itself
       if len(snake_List) > Length_of_snake:
           del snake_List[0]
       
       for x in snake_List[:-1]:
           if x == snake_Head:
               game_close = True
       
       # Draw the snake
       our_snake(snake_block, snake_List)
       # Display the score and level
       Your_score(Length_of_snake - 1, level)
       # Update the display
       pygame.display.update()
       
       # Check if the snake has eaten the food
       if x1 == foodx and y1 == foody:
           # Generate new food position
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           # Increase the length of the snake
           Length_of_snake += 1
           # Increase the snake speed and level every 3rd score
           if ((Length_of_snake - 1) % 3 == 0):
               snake_speed += 3
               level += 1
       
       # Set the frame rate of the game
       clock.tick(snake_speed)
   # Quit pygame and exit the game loop
   pygame.quit()
   quit()

# Call the gameLoop function to start the game
gameLoop()
