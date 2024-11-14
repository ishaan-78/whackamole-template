import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_pos = 0
        y_pos = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(0,640,32):
                pygame.draw.line(screen, 'black', (i, 0), (i, 512))
            for i in range(0,512,32):
                pygame.draw.line(screen, 'black', (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos, y_pos)))
            pygame.display.flip()
            clock.tick(60)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // 32
                col = x // 32
                print(x,y,row,col)
                if row == y_pos//32 and col == x_pos//32:
                    x_pos = random.randrange(0, 640) // 32 * 32
                    y_pos = random.randrange(0, 512) // 32 * 32
                    screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos, y_pos)))
                    print('yes')




    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
