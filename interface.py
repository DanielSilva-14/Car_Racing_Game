import pygame
import sys
import cv2
from pydub import AudioSegment
from choosecar import selection_single, selection_multi1


def play_audio(video_file):
    """Plays audio extracted from a video file using Pygame.
    This function utilizes Pygame's mixer module to play audio extracted from a video file using pydub. It ensures the audio file's frequency and channels are set correctly for smooth playback.

    This function allows the playback of audio extracted from video files in a synchronized manner using Pygame's mixer module.

    Parameters:
    `video_file`: (str) Path to the video file containing the audio to be played

    Returns:
    None: The function does not directly return a value but plays the audio file."""

    video_clip = AudioSegment.from_file(video_file)  # loads audio from a video file using pydub
    pygame.mixer.init(frequency=video_clip.frame_rate, channels=video_clip.channels)  # initializes Pygame mixer with the audio properties
    sound = pygame.mixer.Sound(buffer=video_clip.raw_data)  # creates a Pygame Sound object from the audio data
    sound.play()  # plays the sound


# define a global variable sound_on and a function toggle_sound that toggles the sound state between playing and pausing
sound_on = True


def toggle_sound():
    """Toggles the audio playback state.
    This function manages the audio playback state, allowing players to switch between playing and pausing music. It utilizes the global `sound_on` variable to maintain the current audio playback state.

    This function provides a convenient way for players to manage the audio playback during gameplay, enabling them to customize their audio experience.

    Returns:
    None: The function does not directly return a value but toggles the audio playback. """

    global sound_on
    sound_on = not sound_on
    if sound_on:
        pygame.mixer.unpause()
    else:
        pygame.mixer.pause()


def redirecionar_para_interface():
    """Terminates the current game mode and redirects the player to the interface screen.
    This function serves as a mechanism to transition between different game modes or screens.
    It quits the current game mode, represented by Pygame, and calls the `interface()` function to handle the user interface and game logic accordingly.

    This function provides a clean way to navigate between different game modes or screens without disrupting the overall gameplay experience.

    Returns:
    None: The function does not directly return a value but facilitates the transition between game modes."""

    pygame.quit()
    interface()


def interface():
    """Manages the initial game selection screen, allowing players to choose between single-player or multiplayer modes.

    This function serves as the core of the game's user interface, providing a seamless transition between the initial splash screen and the respective game modes.
    It utilizes Pygame's graphics, event handling, and timing capabilities to create an interactive and engaging selection process.

    This function plays a crucial role in setting the stage for the game, providing a user-friendly interface that guides players towards their chosen game mode.
    It seamlessly integrates with the overall gameplay, ensuring a smooth and engaging experience for users.

    Returns:
    None: The function does not directly return a value but manages the game mode selection and handles user input."""

    # initiating pygames
    pygame.init()

    # creating the screen 720x540 pixels
    res = (720, 540)
    screen = pygame.display.set_mode(res)

    # creating some colors (RGB scale)
    white = (255, 255, 255)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)

    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()

    # create fonts and render text surfaces
    corbel_font = pygame.font.SysFont("stencil", 20)
    game1_text = corbel_font.render('Single player', True, black)
    game2_text = corbel_font.render('Multiplayer', True, black)
    credits_text = corbel_font.render('Credits', True, black)
    quit_text = corbel_font.render('Quit', True, black)

    # load an image for the interface
    title = pygame.image.load("racing.png")
    new_width, new_height = 200, 200
    image = pygame.transform.scale(title, (new_width, new_height))

    # load sound icons for the interface.
    sound_on_icon = pygame.image.load("som.png")
    sound_off_icon = pygame.image.load("semsom.png")
    sound_on_icon = pygame.transform.scale(sound_on_icon, (35, 35))
    sound_off_icon = pygame.transform.scale(sound_off_icon, (35, 35))

    video_file = 'filme.mp4'  # define the video file
    cap = cv2.VideoCapture(video_file)  # set up video capture using OpenCV

    # load an image for the flag
    flag = pygame.image.load("bandeira.png")
    flag = pygame.transform.scale(flag, (800, 50))

    if not cap.isOpened():  # conditional block checks if the video capture was successful. If not, it prints an error message, quits Pygame, and exits the program
        print("Error")
        pygame.quit()
        sys.exit()

    play_audio(video_file)  # play audio
    original_frame_rate = cap.get(cv2.CAP_PROP_FPS)  # get the original frame rate of the video
    clock = pygame.time.Clock()  # set up a Pygame clock

    # define variables for sound changes
    sound_change_delay = 500
    last_sound_change_time = pygame.time.get_ticks()

    # interface loop
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():  # handle Pygame events
            if event.type == pygame.QUIT:  # quitting the program
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # checks if the current event is a mouse button down event
                mouse = pygame.mouse.get_pos()  # this gives you a tuple containing the x and y coordinates of the mouse cursor
                if 670 <= mouse[0] <= 705 and 10 <= mouse[1] <= 45:
                    current_time = pygame.time.get_ticks()  # Gets the current time in milliseconds using "pygame.time.get_ticks()"
                    if current_time - last_sound_change_time > sound_change_delay:  # Checks if enough time has elapsed since the last sound change.
                        toggle_sound()  # If the conditions in the previous line are met, this function is called to toggle the sound state.
                        last_sound_change_time = current_time  # Updates the "last_sound_change_time" to the current time, marking the time of the most recent sound change

            # press on quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(width)
                print(height)
                if 655 <= mouse[0] <= 710 and 500 <= mouse[1] <= 530:
                    pygame.quit()

            # press the credits button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 544 <= mouse[0] <= 637 and 500 <= mouse[1] <= 530:
                    pygame.mixer.stop()
                    credits_()

            # pressing the single button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 182 <= mouse[0] <= 344 and 500 <= mouse[1] <= 520:
                    pygame.mixer.stop()
                    selection_single()

            # pressing the multiplayer button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 363 <= mouse[0] <= 529 and 500 <= mouse[1] <= 530:
                    pygame.mixer.stop()
                    selection_multi1()

        ret, frame = cap.read()  # reads a frame from the video capture object (cap). It returns ret (a boolean indicating whether the frame was successfully read) and frame (the actual frame).

        #  block checks if the frame was not successfully read (probably indicating the end of the video).
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # resets the video capture position to the beginning
            if sound_on:  # If sound is on, the following actions are performed
                pygame.mixer.stop()  # stops the audio
                play_audio(video_file)
                # plays the audio again (to restart it)
                pygame.mixer.unpause()  # Unpauses the audio playback
            if not sound_on:  # If sound is not on, the following actions are performed
                pygame.mixer.stop()  # stops the audio
                play_audio(video_file)  # plays the audio again (to restart it)
                pygame.mixer.pause()  # Pauses the audio playback
            continue  # skip the rest of the loop's code and move to the next iteration of the loop

        if frame.shape[1] > frame.shape[0]:  # block checks if the frame is in landscape orientation
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # rotates it if necessary
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converts the frame from BGR to RGB (Pygame uses RGB format)
            pygame_frame = pygame.surfarray.make_surface(frame)  # creates a Pygame surface from the frame
            pygame_frame = pygame.transform.scale(pygame_frame, (1200, 600))  # scales it to (1200, 600) pixels
            pygame.display.flip()  # flips the Pygame display
            screen.blit(pygame_frame, (-100, -25))  # blit the frame
            screen.blit(flag, (0, 490))  # blit the flag

            # selecting between two values (sound_on_icon and sound_off_icon) based on the condition (boolean) specified by sound_on
        if sound_on:
            sound_icon = sound_on_icon
        else:
            sound_icon = sound_off_icon
        screen.blit(sound_icon, (670, 10))  # blit the sound_icon

        # SINGLE PLAYER
        # draw a rectangle on the screen for the "Single Player" button. If the mouse is over the button, it's drawn in dark gray; otherwise, it's drawn in white
        if 182 <= mouse[0] <= 347 and 500 <= mouse[1] <= 520:
            pygame.draw.rect(screen, color_dark, [182, 500, 165, 30])
            pygame.draw.rect(screen, black, [182, 500, 165, 30], 1)
        else:
            pygame.draw.rect(screen, white, [182, 500, 165, 30])
            pygame.draw.rect(screen, black, [182, 500, 165, 30], 1)
        screen.blit(game1_text, (192, 505))  # the button text is then blit onto the screen

        # MULTIPLAYER
        # draw a rectangle on the screen for the "Multiplayer" button. If the mouse is over the button, it's drawn in dark gray; otherwise, it's drawn in white
        if 363 <= mouse[0] <= 363 + 166 and 500 <= mouse[1] <= 500 + 30:
            pygame.draw.rect(screen, color_dark, [363, 500, 166, 30])
            pygame.draw.rect(screen, black, [363, 500, 166, 30], 1)
        else:
            pygame.draw.rect(screen, white, [363, 500, 166, 30])
            pygame.draw.rect(screen, black, [363, 500, 166, 30], 1)
        screen.blit(game2_text, (378, 505))  # the button text is then blit onto the screen

        # CREDITS
        # draw a rectangle on the screen for the "Credits" button. If the mouse is over the button, it's drawn in dark gray; otherwise, it's drawn in white
        if 544 <= mouse[0] <= 544 + 93 and 500 <= mouse[1] <= 500 + 30:
            pygame.draw.rect(screen, color_dark, [544, 500, 93, 30])
            pygame.draw.rect(screen, black, [544, 500, 93, 30], 1)
        else:
            pygame.draw.rect(screen, white, [544, 500, 93, 30])
            pygame.draw.rect(screen, black, [544, 500, 93, 30], 1)
        screen.blit(credits_text, (548, 505))  # the button text is then blit onto the screen

        # QUIT
        # draw a rectangle on the screen for the "Quit" button. If the mouse is over the button, it's drawn in dark gray; otherwise, it's drawn in white
        if 655 <= mouse[0] <= 655 + 55 and 500 <= mouse[1] <= 500 + 30:
            pygame.draw.rect(screen, color_dark, [655, 500, 55, 30])
            pygame.draw.rect(screen, black, [655, 500, 55, 30], 1)
        else:
            pygame.draw.rect(screen, white, [655, 500, 55, 30])
            pygame.draw.rect(screen, black, [655, 500, 55, 30], 1)
        screen.blit(quit_text, (659, 505))  # the button text is then blit onto the screen

        # TITLE TEXT
        screen.blit(image, (0, 350))  # blit the image (title/logo) onto the screen

        pygame.display.update()  # update the Pygame display
        clock.tick(original_frame_rate)  # regulate the frame rate using the clock

    # When everything done, release the video capture object
    cap.release()

    pygame.quit()


def credits_():
    """Display credits screen with background image and back button.

    Initializes Pygame, creates a window with a specified resolution, loads and scales images,
    and continuously updates the display. The function listens for mouse events, such as clicking
    the back button to return to the main interface or closing the window to exit the system.

    Returns:
    None """

    pygame.init()

    res = (800, 542)  # screen resolution with width 800 pixels and height 542 pixels.
    screen = pygame.display.set_mode(res)  # creates a  window with the specified resolution.

    # load an image named, scale it to the display resolution, and create a rectangle with the same dimensions.
    fundo_credits = pygame.image.load("credits.png")
    fundo_credits = pygame.transform.scale(fundo_credits, res)
    fundo_credits_rect = fundo_credits.get_rect()
    fundo_credits_rect.x = 0
    fundo_credits_rect.y = 0

    # load an image named and scale it to a size of 105x34 pixels.
    back_button = pygame.image.load("back.png")
    back_button = pygame.transform.scale(back_button, (105, 34))

    while True:
        # If the user clicks the mouse button within the region of the back button, it calls the interface() function. If the user closes the window, it exits the system
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 0 + 105 and 500 <= mouse[1] <= 500 + 34:
                    interface()
            elif ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fundo_credits, fundo_credits_rect.topleft)  # draw the background image
        screen.blit(back_button, (0, 500))  # draw the back button

        pygame.display.update()  # updates the Pygame display
