import pygame
import random
import sys
import main
from car import Car
from powerups import Invincibility, Slowing, ChangeCar, Reverse


def game_over_screen(score_value):
    from interface import redirecionar_para_interface
    from choosecar import redirecionar_para_choosecar2

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    SCREENWIDTH = 800
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    end = pygame.image.load("gameover.png")
    end = pygame.transform.scale(end, (800, 600))

    clock = pygame.time.Clock()

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 422.7 <= mouse[0] <= 596.3 and 374.5 <= mouse[1] <= 477:
                    redirecionar_para_choosecar2()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 208.5 <= mouse[0] <= 397.1 and 374.5 <= mouse[1] <= 477:
                    redirecionar_para_interface()

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # GAME OVER
        pygame.draw.rect(screen, WHITE, [190, 300, 300, 100])
        pygame.draw.rect(screen, BLACK, [190, 300, 300, 100], 1)
        screen.blit(end, (0, 0))
        score_font = pygame.font.Font(None, 40)
        score_text = score_font.render(f"{score_value}", True, WHITE)
        screen.blit(score_text, (400, 530))

        pygame.display.update()
        clock.tick(60)


def multi_racing(selectedCar1, selectedCar2):
    pygame.init()

    WHITE = (255, 255, 255)

    main.speed = 1

    SCREENWIDTH = 800
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    road = pygame.image.load("mapa.png").convert_alpha()
    road = pygame.transform.scale(road, (SCREENWIDTH, SCREENHEIGHT))
    border = pygame.image.load("border.png")
    border = pygame.transform.scale(border, (SCREENWIDTH, SCREENHEIGHT))
    border_mask = pygame.mask.from_surface(border)
    pygame.display.set_caption("Car Racing")

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    playerCar = Car(selectedCar1, 70, 80, 70)
    playerCar.rect.x = 360
    playerCar.rect.y = 370

    playerCar2 = Car(selectedCar2, 70, 80, 70)
    playerCar2.rect.x = 360
    playerCar2.rect.y = 370

    car1 = Car("purple", 60, 80, random.randint(50, 100))
    car1.rect.x = 210
    car1.rect.y = -100

    car2 = Car("red", 60, 80, random.randint(50, 100))
    car2.rect.x = 315
    car2.rect.y = -600

    car3 = Car("green", 60, 80, random.randint(50, 100))
    car3.rect.x = 420
    car3.rect.y = -300

    car4 = Car("blue", 60, 80, random.randint(50, 100))
    car4.rect.x = 525
    car4.rect.y = -900

    # Add the car to the list of objects
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(playerCar)
    all_sprites_list.add(playerCar2)

    all_coming_cars = pygame.sprite.Group()

    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    # Create the power ups
    powerup = Invincibility(random.randint(50, 100))
    powerup.rect.x = random.randint(200, 500)
    powerup.rect.y = random.randint(-10000, -200)
    # powerup.rect.x = 420

    powerup2 = Slowing(random.randint(50, 100))
    powerup2.rect.x = random.randint(200, 500)
    powerup2.rect.y = random.randint(-10000, -200)
    # powerup2.rect.x = 300

    powerup3 = ChangeCar(random.randint(50, 100))
    powerup3.rect.x = random.randint(200, 500)
    powerup3.rect.y = random.randint(-10000, -200)
    # powerup3.rect.x = 200

    powerup4 = Reverse(random.randint(50, 100))
    powerup4.rect.x = random.randint(200, 500)
    powerup4.rect.y = random.randint(-10000, -200)
    # powerup4.rect.x = 500

    all_coming_powerups = pygame.sprite.Group()

    all_coming_powerups.add(powerup)
    all_coming_powerups.add(powerup2)
    all_coming_powerups.add(powerup3)
    all_coming_powerups.add(powerup4)

    all_sprites_list.add(all_coming_powerups)

    carryOn = True
    clock = pygame.time.Clock()
    score_value = 0
    font = pygame.font.Font(None, 30)

    # Load the background image
    background = pygame.image.load('mapa.png')
    bg_width, bg_height = background.get_size()
    score = pygame.image.load("score.png").convert_alpha()
    score = pygame.transform.scale(score, (150, 80))
    powerup_active = (False, 0)

    # Initial positions of the two background images
    bg_y = bg_height

    while carryOn:
        screen.blit(road, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

            elif event.type == pygame.USEREVENT + 1:
                playerCar.No_Invencible()

            elif event.type == pygame.USEREVENT + 2:
                playerCar.No_Slower()
                main.speed = 1

            elif event.type == pygame.USEREVENT + 3:
                playerCar.change = False
                playerCar.repaint(isPlayer=True, model=playerCar.original_model)

            elif event.type == pygame.USEREVENT + 4:
                playerCar.No_Reversible()
                main.speed = 1

            elif event.type == pygame.USEREVENT + 5:
                playerCar2.No_Invencible()

            elif event.type == pygame.USEREVENT + 6:
                playerCar2.No_Slower()
                main.speed = 1

            elif event.type == pygame.USEREVENT + 7:
                playerCar2.change = False
                playerCar2.repaint(isPlayer=True, model=playerCar2.original_model)

            elif event.type == pygame.USEREVENT + 8:
                playerCar2.No_Reversible()
                main.speed = 1

        score_text = font.render(f" {score_value} ", True, WHITE)

        # Update the position of the background image
        bg_y += 2
        # Reset position when it goes off-screen
        if bg_y >= bg_height:
            bg_y = 0

        # Draw the background image twice to create a continuous effect
        screen.blit(background, (0, bg_y))
        screen.blit(background, (0, bg_y - bg_height))
        screen.blit(score, (-10, 10))
        screen.blit(score_text, (49.5, 40))

        if playerCar.collision(border_mask) != None:
            playerCar.bounce(border_mask)
        if playerCar2.collision(border_mask) != None:
            playerCar2.bounce(border_mask)

        if playerCar.rect.y <= 0 or playerCar.rect.y >= 600 - playerCar.image.get_height():
            playerCar.bounce_vertical()
        if playerCar2.rect.y <= 0 or playerCar2.rect.y >= 600 - playerCar2.image.get_height():
            playerCar2.bounce_vertical()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(6)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(6)
        if keys[pygame.K_UP]:
            playerCar.moveForward(6)
        if keys[pygame.K_DOWN]:
            playerCar.moveBackward(6)
        if keys[pygame.K_a]:
            playerCar2.moveLeft(6)
        if keys[pygame.K_d]:
            playerCar2.moveRight(6)
        if keys[pygame.K_w]:
            playerCar2.moveForward(6)
        if keys[pygame.K_s]:
            playerCar2.moveBackward(6)

        player_mask = playerCar.new_mask()
        player_mask2 = playerCar2.new_mask()

        for car in all_coming_cars:
            coming_masks = car.new_mask()
            # Check for collision1
            offset1 = (car.rect.x - playerCar.rect.x, car.rect.y - playerCar.rect.y)
            collision1 = player_mask.overlap(coming_masks, offset1)
            offset2 = (car.rect.x - playerCar2.rect.x, car.rect.y - playerCar2.rect.y)
            collision2 = player_mask2.overlap(coming_masks, offset2)
            if collision1 and not playerCar.invincible:
                print("Collision - Player 1")
                # End Of Game
                carryOn = False
                game_over_screen(score_value)
            if collision2 and not playerCar2.invincible:
                print("Collision - Player 2")
                carryOn = False
                game_over_screen(score_value)

        for powerup in all_coming_powerups:
            powerup.powerupMove(main.speed)
            if playerCar.reverse or playerCar2.reverse:
                if powerup.rect.y < -SCREENHEIGHT:
                    powerup.repaint()
                    powerup.rect.y = random.randint(600, 2000)
            elif powerup.rect.y > SCREENHEIGHT:
                powerup.repaint()
                powerup.rect.y = random.randint(-2000, -200)

        # Power up collision
        if powerup_active[0]:
            powerup_active = (True, max(0, powerup_active[1] - clock.get_time() / 1000.0))
            if powerup_active[1] <= 0:
                powerup_active = (False, 0)
                main.speed = 1

        # Power up collision
        if not powerup_active[0] or powerup_active[1] <= 0:
            for powerup in all_coming_powerups:
                coming_masks = powerup.new_mask()
                # Check for collision
                offset1 = (powerup.rect.x - playerCar.rect.x, powerup.rect.y - playerCar.rect.y)
                collision1 = player_mask.overlap(coming_masks, offset1)
                offset2 = (powerup.rect.x - playerCar2.rect.x, powerup.rect.y - playerCar2.rect.y)
                collision2 = player_mask2.overlap(coming_masks, offset2)
                if collision1:
                    print("Collision")
                    powerup.activate(playerCar)
                    powerup.repaint(playerCar.reverse)
                    new_powerup = random.choice(powerup.availablePowerUps)(main.speed)  # change to another type of power up
                    powerup_active = (True, new_powerup.duration)
                    all_coming_powerups.add(new_powerup)
                    print(powerup)
                    break
                if collision2:
                    print("Collision")
                    powerup.activate(playerCar2, True)
                    powerup.repaint(playerCar2.reverse)
                    new_powerup2 = random.choice(powerup.availablePowerUps)(main.speed)  # change to another type of power up
                    powerup_active = (True, new_powerup2.duration)
                    all_coming_powerups.add(new_powerup2)
                    print(powerup)
                    break
            else:
                powerup_active = (False, 0)

        for powerup in all_coming_powerups:
            powerup.draw_countdown(screen)

        for car in all_coming_cars:
            car.trafficMove(main.speed)
            if playerCar.reverse or playerCar2.reverse:
                if playerCar.slowing or playerCar2.slowing:
                    main.speed = 0.8
                elif car.rect.y < -SCREENHEIGHT:
                    car.repaint()
                    car.changeSpeed(random.randint(50, 100))
                    car.rect.y = random.randint(600, 1000)
                    if car.rect.y > SCREENHEIGHT:
                        pass
                    else:
                        score_value += 1
            elif car.rect.y > SCREENHEIGHT:
                car.repaint()
                car.changeSpeed(random.randint(50, 100))
                car.rect.y = random.randint(-2000, -200)
                score_value += 1


        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per secong e.g. 60
        clock.tick(60)
