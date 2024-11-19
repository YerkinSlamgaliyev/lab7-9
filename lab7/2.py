import pygame
import datetime

pygame.init()

WIDTH = 1300
HEIGHT = 1000
FPS = 60

background = pygame.image.load('C:/Users/slamg/OneDrive/Рабочий стол/pp2/lab7/mickeyclock.jpg')
minute = pygame.image.load('C:/Users/slamg/OneDrive/Рабочий стол/pp2/lab7/minuthand.png')
second = pygame.image.load('C:/Users/slamg/OneDrive/Рабочий стол/pp2/lab7/secondhand.png')

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

time = datetime.datetime.now()
angle = -(int(time.strftime("%S")) * 6) - 6
angleM = -(int(time.strftime("%M")) * 6 + (int(time.strftime("%S")) * 6 / 60)) - 54

orig_image = second
rect = orig_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

orig_imagem = minute
rect1 = orig_imagem.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = datetime.datetime.now()
    angle = -(int(time.strftime("%S")) * 6) - 6
    angleM = -(int(time.strftime("%M")) * 6 + (int(time.strftime("%S")) * 6 / 60)) - 54

    screen.blit(background, (0, 0))
    image, rect = rotate(orig_image, rect, angle)
    imagem, rect1 = rotate(orig_imagem, rect1, angleM)
    
    screen.blit(image, rect)
    screen.blit(imagem, rect1)

    pygame.display.flip()

pygame.quit()
