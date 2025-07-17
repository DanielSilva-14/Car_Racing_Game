import pygame
import sys
from game import car_racing
from multiplayer import multi_racing


def redirecionar_para_choosecar1():
    """Terminates the current Pygame application and redirects the player to the choosecar screen.

    This function serves as a redirection point, closing the current game session and initiating the selection process for a new game.
    It utilizes the `pygame.quit()` function to terminate the Pygame application and then calls the `selection_single()` function to display the choosecar screen.

    Returns:
    None: This function does not directly return a value. It terminates the current Pygame application and initiates the selection process."""

    pygame.quit()
    selection_single()


def redirecionar_para_choosecar2():
    """Terminates the current Pygame application and redirects the player to the choosecar screen for multiplayer mode.

    This function serves as a redirection point, closing the current game session and initiating the selection process for a multiplayer game.
    It utilizes the `pygame.quit()` function to terminate the Pygame application and then calls the `selection_multi1()` function to display the multiplayer choose car screen.

    Returns:
    None: This function does not directly return a value. It terminates the current Pygame application and initiates the multiplayer selection process."""

    pygame.quit()
    selection_multi1()


def selection_single():
    """Manages the single-player mode car selection screen, providing options to choose a car, return to the interface, and view instructions.
    This function creates and manages the single-player mode car selection screen, providing a user interface for choosing a car and starting the game.
    It utilizes pygame's graphics, event handling, and timing capabilities to create an interactive and user-friendly selection screen.

    Returns:
    None: This function does not directly return a value. It manages the car selection process and handles user input."""

    from interface import redirecionar_para_interface
    pygame.init()

    # set up the Pygame display with a resolution of 600x540 pixels.
    res = (600, 540)
    screen = pygame.display.set_mode(res)

    # load images for the background, back button, and start button with specified dimensions.
    cars = pygame.image.load("choosecar.png")
    cars = pygame.transform.scale(cars, (600, 540))
    back_button = pygame.image.load("back.png")
    back_button = pygame.transform.scale(back_button, (105, 34))
    start_button = pygame.image.load("start.png")
    start_button = pygame.transform.scale(start_button, (105, 35))

    instruction = pygame.image.load("Instructions.png").convert_alpha()
    instruction = pygame.transform.scale(instruction, (600, 540))

    model_list = ["yellow", "branco", "azul", "purpleplayer", "vermelho"]  # defines a list of car models
    current_index = 0  # initializes the current index to 0
    current_image = pygame.image.load("car." + model_list[current_index] + ".png")  # loads the image of the current car model
    image_rect = current_image.get_rect(center=(res[0] // 2, res[1] // 2))  # gets its rectangle for positioning

    clock = pygame.time.Clock()  # set up a Pygame clock for controlling the frame rate
    running = True

    while running:  # a loop that will run until the running flag is set to "False"
        # checks for events, including mouse clicks. Updates current_index based on mouse clicks and calls the appropriate functions for other buttons.
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 145.4 <= mouse[0] <= 145.4 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index - 1) % len(model_list)
                elif 384.6 <= mouse[0] <= 384.6 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index + 1) % len(model_list)
                elif 0 <= mouse[0] <= 0 + 105 and 500 <= mouse[1] <= 500 + 34:
                    redirecionar_para_interface()
                elif 495 <= mouse[0] <= 495 + 105 and 500 <= mouse[1] <= 500 + 35:
                    screen.blit(instruction, (0, 0))  # Display the image

                    pygame.display.flip()  # Update the display
                    pygame.time.wait(1000)  # Wait for 1 second (adjust as needed)
                    pygame.event.clear()  # Clear events to avoid immediate key press detection

                    # Wait for a key press to start the game
                    key_pressed = False

                    while not key_pressed:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                key_pressed = True
                            elif event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                    car_racing(model_list[current_index])

        # draw the background and buttons
        screen.blit(cars, (0, 0))
        screen.blit(back_button, (0, 500))
        screen.blit(start_button, (495, 500))

        # updates the current car image and draws it
        current_image = pygame.image.load("car." + model_list[current_index] + ".png")
        screen.blit(current_image, image_rect)

        pygame.display.flip()  # update the display
        clock.tick(60)  # control the frame rate

def selection_multi1():
    """Manages the first stage of the multiplayer mode car selection screen, providing options to choose a car and return to the interface.
    This function serves as the first stage of the multiplayer mode car selection process, allowing the first player to select their car.
    It utilizes pygame's graphics, event handling, and timing capabilities to create an interactive and user-friendly selection screen.

    Returns:
    None: This function does not directly return a value. It manages the car selection process and handles user input."""

    from interface import redirecionar_para_interface
    pygame.init()

    # set up the Pygame display with a resolution of 600x540 pixels.
    res = (600, 540)
    screen = pygame.display.set_mode(res)

    # load images for the background, back button, and start button with specified dimensions.
    cars = pygame.image.load("choosecar1.png")
    cars = pygame.transform.scale(cars, (600, 540))
    back_button = pygame.image.load("back.png")
    back_button = pygame.transform.scale(back_button, (105, 34))
    start_button = pygame.image.load("start.png")
    start_button = pygame.transform.scale(start_button, (105, 35))

    instruction = pygame.image.load("Instructions.png").convert_alpha()
    instruction = pygame.transform.scale(instruction, (600, 540))

    model_list = ["yellow", "branco", "azul", "purpleplayer", "vermelho"]  # defines a list of car models
    current_index = 0  # initializes the current index to 0
    current_image = pygame.image.load("car." + model_list[current_index] + ".png")  # loads the image of the current car model
    image_rect = current_image.get_rect(center=(res[0] // 2, res[1] // 2))  # gets its rectangle for positioning

    clock = pygame.time.Clock()  # set up a Pygame clock for controlling the frame rate
    running = True
    while running:  # a loop that will run until the running flag is set to "False"
        # checks for events, including mouse clicks. Updates current_index based on mouse clicks and calls the appropriate functions for other buttons.
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 145.4 <= mouse[0] <= 145.4 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index - 1) % len(model_list)  # Decreases the current_index by 1, and wraps around to the end if it becomes negative.
                elif 384.6 <= mouse[0] <= 384.6 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index + 1) % len(model_list)  # Increases the current_index by 1, and wraps around to the beginning if it exceeds the length of model_list.
                elif 0 <= mouse[0] <= 0 + 105 and 500 <= mouse[1] <= 500 + 34:
                    redirecionar_para_interface()
                elif 495 <= mouse[0] <= 495 + 105 and 500 <= mouse[1] <= 500 + 35:
                    selection_multi2(selectedCar1=model_list[current_index])  # Calls the function selection_multi2() with the argument selectedCar1 set to the value at the current index of model_list.

        # draw the background and buttons
        screen.blit(cars, (0, 0))
        screen.blit(back_button, (0, 500))
        screen.blit(start_button, (495, 500))

        # updates the current car image and draws it
        current_image = pygame.image.load("car." + model_list[current_index] + ".png")
        screen.blit(current_image, image_rect)

        pygame.display.flip()  # update the display
        clock.tick(60)  # control the frame rate


def selection_multi2(selectedCar1):
    """Manages the second stage of the multiplayer mode car selection screen, allowing players to choose their cars and start the game.

    This function serves as the second stage of the multiplayer mode car selection process, allowing the remaining players to choose their cars.
    It utilizes pygame's graphics, event handling, and timing capabilities to create an interactive and user-friendly selection screen.

    Returns:
    None: This function does not directly return a value. It manages the car selection process and handles user input."""

    pygame.init()

    # set up the Pygame display with a resolution of 600x540 pixels.
    res = (600, 540)
    screen = pygame.display.set_mode(res)

    # load images for the background, back button, and start button with specified dimensions.
    cars = pygame.image.load("choosecar2.png")
    cars = pygame.transform.scale(cars, (600, 540))
    back_button = pygame.image.load("back.png")
    back_button = pygame.transform.scale(back_button, (105, 34))
    start_button = pygame.image.load("start.png")
    start_button = pygame.transform.scale(start_button, (105, 35))

    instruction = pygame.image.load("Instructions.png").convert_alpha()
    instruction = pygame.transform.scale(instruction, (600, 540))

    model_list = ["yellow", "branco", "azul", "purpleplayer", "vermelho"]  # defines a list of car models
    current_index = 0  # initializes the current index to 0
    current_image = pygame.image.load("car." + model_list[current_index] + ".png")  # loads the image of the current car model
    image_rect = current_image.get_rect(center=(res[0] // 2, res[1] // 2))  # gets its rectangle for positioning

    clock = pygame.time.Clock()  # set up a Pygame clock for controlling the frame rate
    running = True
    while running:  # a loop that will run until the running flag is set to "False"
        # checks for events, including mouse clicks. Updates current_index based on mouse clicks and calls the appropriate functions for other buttons.
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 145.4 <= mouse[0] <= 145.4 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index - 1) % len(model_list)
                elif 384.6 <= mouse[0] <= 384.6 + 60.1 and 446.8 <= mouse[1] <= 446.8 + 57:
                    current_index = (current_index + 1) % len(model_list)
                elif 0 <= mouse[0] <= 0 + 105 and 500 <= mouse[1] <= 500 + 34:
                    redirecionar_para_choosecar2()
                elif 495 <= mouse[0] <= 495 + 105 and 500 <= mouse[1] <= 500 + 35:
                    screen.blit(instruction, (0, 0))  # Display the image
                    pygame.display.flip()  # Update the display
                    pygame.time.wait(1000)  # Wait for 1 second (adjust as needed)
                    pygame.event.clear()  # Clear events to avoid immediate key press detection

                    # Wait for a key press to start the game
                    key_pressed = False
                    while not key_pressed:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                key_pressed = True
                            elif event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                    multi_racing(selectedCar1, model_list[current_index])

        # draw the background and buttons
        screen.blit(cars, (0, 0))
        screen.blit(back_button, (0, 500))
        screen.blit(start_button, (495, 500))

        # updates the current car image and draws it
        current_image = pygame.image.load("car." + model_list[current_index] + ".png")
        screen.blit(current_image, image_rect)

        pygame.display.flip()  # update the display
        clock.tick(60)  # control the frame rate


pygame.quit()
