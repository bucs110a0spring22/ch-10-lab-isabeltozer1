import sys
import pygame
import random
from src import hero
from src import enemy
from src import heart


class Controller:
    def __init__(self, width=640, height=480):
        '''Initializes the controller
      args: self, width (int), height(int)'''
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        self.heart = heart.heart("assets/heart.jpg")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies) + (self.heart,))
        self.state = "GAME"

    def mainLoop(self):
        '''The main loop of the game
      args: self'''
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if fights:
                for e in fights:
                    if self.hero.fight(e):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)
            else:
                self.background.fill((250,250,250))
                
            healed = self.hero.rect.colliderect(self.heart.rect)
            if healed :
                self.Hero.heal()
                self.background.fill((250,250,250))
                num_enemies = random.randrange(1,10)
                for i in range(num_enemies):
                  x = random.randrange(100, 400)
                  y = random.randrange(100, 400)
                  e = enemy.Enemy("Boogie", x, y, 'assets/enemy.png')
                  self.heart.rect.x = self.hero.rect.x + self.hero.width + 5
                  self.heart.rect.y = self.hero.rect.y + self.hero.height + 5
                  self.enemies.add(e)
                  self.all_sprites.add(e)
            
                    
            self.enemies.update()
            self.heart.update()

            
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
                
            # redraw the entire screen
            self.screen.blit(self.background, (0, 0)) 
            self.all_sprites.draw(self.screen)

            

            # update the screen
            pygame.display.flip()

    def gameOver(self):
        '''The game over loop
      args: self'''
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
