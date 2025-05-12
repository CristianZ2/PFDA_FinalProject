import pygame
import sys
import random


WIDTH = 800
HEIGHT = 600


cars = []

# Coordinates of each lane
lane_one_Y = 200
lane_two_Y = 290
lane_three_Y = 365
lane_four_Y= 455




class PlayerObject():

    def __init__(self, pos=(200, 200), sprite_path=''):
        self.pos= pos
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect(topleft= self.pos)
        self.speed = 5.0
       
    def move(self, dir):
        self.pos = self.pos + dir * self.speed
        self.pos.x = max(0, min(WIDTH - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(HEIGHT - self.rect.height, self.pos.y))
        self.rect.topleft = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)    

class CarObject():
    def __init__(self, pos=(100, 100), speed = 5.0, image_path=''):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 75))
        self.image = pygame.transform.rotate(self.image, (90))
       
        if speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(topleft= pos)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)    

    def create_cars():
        cars = []
        num_cars = 3
        spacing = WIDTH // num_cars
        image_paths = ["pixel_bluecar.png", "pixel_redcar.png", "pixel_SUV.png"]

        # Give each it lane its coordinate and space out each car
        for lane_four in range(3):
            x = random.randint(0, WIDTH)
            x = lane_four * spacing
            img = random.choice(image_paths)
            cars.append(CarObject(pos=(x, lane_one_Y), speed=5, image_path=img))

        for lane_three in range(3):
            x = random.randint(0, WIDTH)
            x = lane_three * spacing
            img = random.choice(image_paths)
            cars.append(CarObject(pos=(x, lane_two_Y), speed=4, image_path=img))

        for lane_two in range(3):
            x = random.randint(0, WIDTH)
            x = lane_two * spacing
            img = random.choice(image_paths)
            cars.append(CarObject(pos=(x, lane_three_Y), speed=-2, image_path=img))

        for lane_one in range(3):
            x = random.randint(0, WIDTH)
            x = lane_one * spacing
            img = random.choice(image_paths)
            cars.append(CarObject(pos=(x, lane_four_Y), speed=-3, image_path=img))

        return cars




def reset_game():
    player = PlayerObject(pos= (250, 528), sprite_path= "pixel_turtle.png")
    cars = CarObject.create_cars()
    return player, cars


def main():
    pygame.init()
    pygame.display.set_caption("Road Kill")

    # Render font with color and size
    game_over_font = pygame.font.Font('Sectar.otf', 60)
    game_over_box = game_over_font.render("You Got Ran Over!", True, (255, 0, 0))

    win_font = pygame.font.Font('Sectar.otf', 60)
    win_box = win_font.render("You Made It!", True, (0, 200, 0))

    # Font for the scoreboard
    score_font = pygame.font.Font('HopeCity.otf', 40)


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Display road image
    play_area = pygame.image.load("pixel_road.jpg").convert()
    play_area = pygame.transform.scale(play_area, (200,500))

    # Display beach image 
    win_area = pygame.image.load("pixel_beach.jpg").convert()
    win_area = pygame.transform.scale(win_area, (800,100))
    win_rect = pygame.Rect(0,0, WIDTH, 100)

    # Display player image
    player = PlayerObject(pos=(250, 528),
                          sprite_path="pixel_turtle.png")
    player.image = pygame.transform.scale(player.image, (75, 75))

    player, cars = reset_game()

    # score starts at 0
    score = 0

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player Movement input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(pygame.Vector2(0, -1))
        if keys[pygame.K_DOWN]:
            player.move(pygame.Vector2(0, 1))
        if keys[pygame.K_LEFT]:
            player.move(pygame.Vector2(-1, 0))
        if keys[pygame.K_RIGHT]:
            player.move(pygame.Vector2(1, 0))

        # Refresh the screen with tile road image
        for x in range(0, WIDTH, play_area.get_width()):
            for y in range(100, HEIGHT, play_area.get_height()):
                screen.blit(play_area, (x, y))

        # Render & Display
        screen.blit(win_area, (0, 0))

        # player hit box radius
        collision_box_rect = player.rect.inflate(-40, -40)

        # Game will reset and display lose prompt
        for enemy in cars:
            enemy.move()
            enemy.draw(screen)
            if collision_box_rect.colliderect(enemy.rect):

                # Creates losing prompt with color and size

                lose_display_box = game_over_box.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                pygame.draw.rect(screen, (0,0,0), lose_display_box.inflate(60, 200))
                pygame.draw.rect(screen, (255, 0, 0), lose_display_box.inflate(60, 200), 3)

                screen.blit(game_over_box, lose_display_box)
                pygame.display.flip()
                pygame.time.delay(5000)
                player, cars = reset_game()
                score = 0
                break
                
        # creates winning prompt with color and size and keep track of score
        if  collision_box_rect.colliderect(win_rect):
            score += 1
            win_display_box = win_box.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            pygame.draw.rect(screen, (0,0,0), win_display_box.inflate(60, 200))
            pygame.draw.rect(screen, (0, 200, 0), win_display_box.inflate(60, 200), 3)


            screen.blit(win_box, win_display_box)
            pygame.display.flip()
            pygame.time.delay(5000)
            player, cars = reset_game()
            continue

        # Display the scoreboard    
        scoreboard = score_font.render(f"Score- {score}", True, (255, 255, 255))
        screen.blit(scoreboard, (340, 0))

        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()





if __name__ == "__main__":
    main()
