import pygame
import os

pygame.mixer.init()
pygame.init()

music_folder = r"C:\Users\slamg\Downloads\Telegram Desktop"
music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]



screen_width = 500
screen_height = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
                        
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

button_width = 100
button_height = 50
buttons = {
    "prev": pygame.Rect(50, 200, button_width, button_height),
    "play": pygame.Rect(160, 200, button_width, button_height),
    "stop": pygame.Rect(270, 200, button_width, button_height),
    "next": pygame.Rect(380, 200, button_width, button_height)
}

current_track_index = 0
playing = False

def load_track(index):
    global playing
    pygame.mixer.music.load(os.path.join(music_folder, music_files[index]))
    pygame.mixer.music.play()
    playing = True
    print(f"Now playing: {music_files[index]}")

def stop_music():
    pygame.mixer.music.stop()
    global playing
    playing = False
    print("Music stopped.")

load_track(current_track_index)

font = pygame.font.Font(None, 30)

running = True
while running:
    screen.fill(WHITE)
    
    track_name = font.render(f"Track: {music_files[current_track_index]}", True, BLACK)
    screen.blit(track_name, (20, 150))
    
    pygame.draw.rect(screen, BLUE, buttons["prev"])
    pygame.draw.rect(screen, BLUE, buttons["play"])
    pygame.draw.rect(screen, BLUE, buttons["stop"])
    pygame.draw.rect(screen, BLUE, buttons["next"])
    
    prev_text = font.render("Prev", True, WHITE)
    play_text = font.render("Play/ Pause", True, WHITE)
    stop_text = font.render("Stop", True, WHITE)
    next_text = font.render("Next", True, WHITE)
    
    screen.blit(prev_text, (buttons["prev"].x + 15, buttons["prev"].y + 10))
    screen.blit(play_text, (buttons["play"].x + 5, buttons["play"].y + 10))
    screen.blit(stop_text, (buttons["stop"].x + 20, buttons["stop"].y + 10))
    screen.blit(next_text, (buttons["next"].x + 20, buttons["next"].y + 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["play"].collidepoint(event.pos):
                if not playing:
                    pygame.mixer.music.unpause()
                    playing = True
                    print("Music resumed.")
                else:
                    pygame.mixer.music.pause()
                    playing = False
                    print("Music paused.")
            elif buttons["stop"].collidepoint(event.pos):
                pygame.quit()
            elif buttons["next"].collidepoint(event.pos):
                current_track_index = (current_track_index + 1) % len(music_files)
                load_track(current_track_index)
            elif buttons["prev"].collidepoint(event.pos):
                current_track_index = (current_track_index - 1) % len(music_files)
                load_track(current_track_index)
    
    pygame.display.flip()

pygame.quit()
