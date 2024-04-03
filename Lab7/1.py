import pygame
from time import localtime as now 
pygame.init()

def get_time():
    global minute, second
    minute, second = now().tm_min, now().tm_sec
get_time()

screen_h = 675
screen_w = 900
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Mickey mouse')


img_main = pygame.image.load('images\\mainclock.png')
img_main = pygame.transform.scale(img_main, (screen_w, screen_h))
img_left = pygame.image.load('images\\leftarm.png')
img_left = pygame.transform.scale(img_left, (45, screen_h))
img_right = pygame.image.load('images\\rightarm.png')
img_right = pygame.transform.scale(img_right, (screen_w, screen_h))

def print_img_by_degree(image, degree): # function for drawing image by given degree
    image = pygame.transform.rotate(image, degree) # at first rotate
    rect = image.get_rect() # create rect object with legth same with image
    rect.center = win.get_rect().center # sets center coord ro rect object
    win.blit(image, rect) # draw image onto win in the position defined by rect
clock = pygame.time.Clock()
run = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
    win.blit(img_main, (0, 0))
    get_time()
    print_img_by_degree(img_left, -second*6 - (0.7 if second>30 else +1.2)) #-0.7/-1.2 used to normalize line
    print_img_by_degree(img_right, -minute*6 -40) #-40 used to normalize line
    pygame.display.update()
    clock.tick(60)