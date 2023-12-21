import pygame

pygame.init()

display_screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption('Bao hong tim me')

game_paused = False

custom_font = pygame.font.Font(r"assets\font\VCR_OSD_MONO_1.001.ttf", 48)

TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display_screen.blit(img, (x, y))
    
gameRunning = True
while gameRunning:
    display_screen.fill((52,89,91))
    
    if game_paused:
        pass
    else:    
        draw_text("Press space to start", custom_font, TEXT_COL, 420, 250)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                display_screen.fill((255,0,0))
        if event.type == pygame.QUIT:
            gameRunning = False
        
        pygame.display.update()

pygame.quit()