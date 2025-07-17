import pygame
import random
import sys
import main
from car import Car
from powerups import Invincibility, Slowing, ChangeCar, Reverse


def game_over_screen(score_value):
    """Displays the game over screen with the final score and provides options to return to the choose car or interface screens.

    Parameters:
    score_value (int): The player's final score.

    This function creates and manages the game over screen, displaying a message indicating the game's end. It also shows the player's final score and provides two buttons:
    1. Return to Choose Car
    2. Return to Interface

    Returns:
    None: This function does not directly return a value. It updates the game screen and handles user input until the player chooses an option."""

    from choosecar import redirecionar_para_choosecar1  # Imports the redirecionar_para_choosecar1 function from the choosecar module
    from interface import redirecionar_para_interface  # Imports the redirecionar_para_interface function from the interface module

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    SCREENWIDTH = 800
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)  # Creates a tuple size representing the dimensions of the game screen
    screen = pygame.display.set_mode(size)  # Initializes a Pygame window with the specified dimensions
    end = pygame.image.load("gameover.png")
    end = pygame.transform.scale(end, (800, 600))

    clock = pygame.time.Clock()  # Initializes a Pygame clock object to regulate the frame rate

    while True:
        mouse = pygame.mouse.get_pos()  # Retrieves the current position of the mouse cursor
        for event in pygame.event.get():  # Iterates through the list of Pygame events
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks if a mouse button has been pressed
                if 422.7 <= mouse[0] <= 596.3 and 374.5 <= mouse[1] <= 477:  # Checks if the mouse cursor is within a specific region on the screen
                    redirecionar_para_choosecar1()  # Calls the function to redirect the player to the "Choose Car" screen

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 208.5 <= mouse[0] <= 397.1 and 374.5 <= mouse[1] <= 477:
                    redirecionar_para_interface()  # Calls the function to redirect the player to the main interface screen

            elif event.type == pygame.QUIT:  # Checks if the user has closed the game window
                pygame.quit()  # Quits the Pygame module
                sys.exit()  # Exits the Python script

        # GAME OVER
        pygame.draw.rect(screen, WHITE, [190, 300, 300, 100])
        pygame.draw.rect(screen, BLACK, [190, 300, 300, 100], 1)
        screen.blit(end, (0, 0))
        score_font = pygame.font.Font(None, 40)
        score_text = score_font.render(f"{score_value}", True, WHITE)
        screen.blit(score_text, (400, 530))

        pygame.display.update()  # Updates the Pygame display.
        clock.tick(60)  # Regulates the frame rate to 60 frames per second


def car_racing(selectedCar1):
    """Car Racing Game Loop
       This function initializes and runs the main game loop for a car racing game using Pygame.

       Parameters
       selectedCar1 : str
        (The model of the player's car)

       Returns
       None

       The function continuously runs the game loop until the player decides to quit."""

    pygame.init()

    WHITE = (255, 255, 255)

    main.speed = 1  # Sets the initial speed of the game

    SCREENWIDTH = 800
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)  # Creates a tuple size representing the dimensions of the game screen
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  # Initializes a Pygame window in fullscreen mode with the specified dimensions
    road = pygame.image.load("mapa.png").convert_alpha()  # Loads an image named "mapa.png" with alpha channel (transparency)
    road = pygame.transform.scale(road, (SCREENWIDTH, SCREENHEIGHT))  # Scales the loaded road image to match the screen dimensions
    border = pygame.image.load("border.png")
    border = pygame.transform.scale(border, (SCREENWIDTH, SCREENHEIGHT))
    border_mask = pygame.mask.from_surface(border)  # Creates a collision mask from the border image
    pygame.display.set_caption("Car Racing")  # Sets the window caption

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    playerCar = Car(selectedCar1, 70, 80, 70)  # Creates a player car object with the specified parameters
    playerCar.rect.x = 360
    playerCar.rect.y = 370

    car1 = Car("purple", 60, 80, random.randint(50, 100))  # Creates an AI-controlled car with random speed
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

    all_coming_cars = pygame.sprite.Group()  # Creates a group specifically for the AI-controlled cars

    # add AI cars to the group
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    # Create the power ups
    powerup = Invincibility(random.randint(50, 100))
    powerup.rect.x = random.randint(200, 500)
    powerup.rect.y = random.randint(-10000, -200)

    powerup2 = Slowing(random.randint(50, 100))
    powerup2.rect.x = random.randint(200, 500)
    powerup2.rect.y = random.randint(-10000, -200)

    powerup3 = ChangeCar(random.randint(50, 100))
    powerup3.rect.x = random.randint(200, 500)
    powerup3.rect.y = random.randint(-10000, -200)

    powerup4 = Reverse(random.randint(50, 100))
    powerup4.rect.x = random.randint(200, 500)
    powerup4.rect.y = random.randint(-10000, -200)

    all_coming_powerups = pygame.sprite.Group()

    all_coming_powerups.add(powerup)
    all_coming_powerups.add(powerup2)
    all_coming_powerups.add(powerup3)
    all_coming_powerups.add(powerup4)

    all_sprites_list.add(all_coming_powerups)  # Adds the powerups to the list of game sprites

    carryOn = True
    clock = pygame.time.Clock()
    score_value = 0
    font = pygame.font.Font(None, 30)

    # Load the background image, sets up variables for the scrolling background effect
    background = pygame.image.load('mapa.png')
    bg_width, bg_height = background.get_size()  # Retrieves and assigns the width and height of the background image
    score = pygame.image.load("score.png").convert_alpha()
    score = pygame.transform.scale(score, (150, 80))
    powerup_active = (False, 0)  # Initializes a tuple (powerup_active) to keep track of whether a powerup is active and its remaining duration

    # Initial positions of the two background images
    bg_y = bg_height

    while carryOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Checks for the QUIT event to exit the game
                carryOn = False

            # Handles custom USEREVENT events (1 to 4) and triggers corresponding actions in the playerCar object and updates game parameters
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

        screen.blit(road, (0, 0))
        score_text = font.render(f" {score_value} ", True, WHITE)  # Renders the score value as text using the specified font and color

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

        # Checks for collisions between the player car and the border, handling bouncing if a collision occurs
        if playerCar.collision(border_mask) != None:
            playerCar.bounce(border_mask)

        # Checks if the player car goes out of the screen vertically, handling bouncing
        if playerCar.rect.y <= 0 or playerCar.rect.y >= 600 - playerCar.image.get_height():
            playerCar.bounce_vertical()

        # Handles player car movement based on key presses.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(6)

        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(6)

        if keys[pygame.K_UP]:
            playerCar.moveForward(6)

        if keys[pygame.K_DOWN]:
            playerCar.moveBackward(6)

        player_mask = playerCar.new_mask()  # Creates a collision mask for the player car

        for car in all_coming_cars:  # Checks for collisions between the player car and AI-controlled cars, triggering the end of the game if a collision occurs
            coming_masks = car.new_mask()
            # Check for collision
            offset = (car.rect.x - playerCar.rect.x, car.rect.y - playerCar.rect.y)  # Calculates the offset between the player car and the current AI-controlled car
            collision = player_mask.overlap(coming_masks, offset)  # Checks for a collision between the player car and the current AI-controlled car using the masks and offset
            if collision and not playerCar.invincible:  # Checks if a collision occurred and the player car is not invincible
                print("Collision")
                # End Of Game
                carryOn = False  # signaling the end of the game loop
                game_over_screen(score_value)  # Calls a function to display the game over screen with the final score

        for powerup in all_coming_powerups:
            powerup.powerupMove(main.speed)  # Moves the powerup based on the game speed
            if playerCar.reverse:  # Checks if the player car is in reverse mode
                if powerup.rect.y < -SCREENHEIGHT:  # If the powerup is above the screen, repaints it and places it at a random position below the screen
                    powerup.repaint()
                    powerup.rect.y = random.randint(600, 2000)
            elif powerup.rect.y > SCREENHEIGHT:  # If the powerup is below the screen, repaints it and places it at a random position above the screen
                powerup.repaint()
                powerup.rect.y = random.randint(-2000, -200)

        # Power up collision
        if powerup_active[0]:  # Checks if a powerup is currently active
            powerup_active = (True, max(0, powerup_active[1] - clock.get_time() / 1000.0))  # Updates the remaining duration of the active powerup
            if powerup_active[1] <= 0:  # If the active powerups duration has expired, deactivates it and resets the game speed
                powerup_active = (False, 0)
                main.speed = 1

        if not powerup_active[0] or powerup_active[1] <= 0:  # If no powerup is currently active or its duration has expired, checks for collisions with new powerups
            for powerup in all_coming_powerups:
                coming_masks = powerup.new_mask()  # Creates a collision mask for the current powerup
                # Check for collision
                offset = (powerup.rect.x - playerCar.rect.x, powerup.rect.y - playerCar.rect.y)  # Calculates the offset between the player car and the current powerup.
                collision = player_mask.overlap(coming_masks, offset)  # Checks for a collision between the player car and the current powerup
                if collision:  # If a collision occurs, activates the powerup, updates the active powerup state, and adds a new random powerup
                    print("Collision")
                    powerup.activate(playerCar)
                    powerup.repaint(playerCar.reverse)
                    powerup_active = (True, powerup.duration, powerup)
                    new_powerup = random.choice(powerup.availablePowerUps)(main.speed)  # change to another type of power up
                    all_coming_powerups.add(new_powerup)
                    print(powerup)
                    break
            else:  # If no collision occurs, sets the active powerup state to indicate no active powerup
                powerup_active = (False, 0)

        # Draws the countdown of the remaining duration for each active powerup on the screen
        for powerup in all_coming_powerups:
            powerup.draw_countdown(screen)

        for car in all_coming_cars:
            car.trafficMove(main.speed)  # Moves the car based on the current game speed
            if playerCar.reverse:  # Checks if the player car is in reverse mode
                if playerCar.slowing:  # Checks if the player car is slowing down
                    main.speed = 0.8  # If slowing down, reduces the game speed
                elif car.rect.y < -SCREENHEIGHT:  # If the car is above the screen, repaints it, changes its speed, and places it at a random position below the screen
                    car.repaint()
                    car.changeSpeed(random.randint(50, 100))
                    car.rect.y = random.randint(600, 1000)
                    if car.rect.y > SCREENHEIGHT:
                        pass
                    else:
                        score_value += 1  # Increments the score when a car goes off the screen
            elif car.rect.y > SCREENHEIGHT:  # If the car is below the screen, repaints it, changes its speed, and places it at a random position above the screen
                car.repaint()
                car.changeSpeed(random.randint(50, 100))
                car.rect.y = random.randint(-2000, -200)
                score_value += 1

        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(60)
