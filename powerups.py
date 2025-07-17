import pygame
import random
import main


class PowerUp(pygame.sprite.Sprite):
    """PowerUp class represents a powerup object in the game.

    Attributes:
    image: Scaled powerup image.
    rect: Powerup rectangular hitbox.
    speed: Powerup movement speed.
    spawnLocationsX: List of x-coordinates for powerup spawning positions.
    availablePowerUps: List of available powerup types.
    activation_time: Time remaining for the powerup effect.

    Methods:
    activate: Activates the powerup effect for the player.
    deactivate: Disables the powerup effect for the player.
    changeSpeed: Updates the powerups movement speed.
    powerupMove: Moves the powerup object across the screen.
    new_mask: Creates a new mask object for the powerups image.
    repaint: Repositions the powerup object and respawns it.
    draw_countdown: Draws the countdown timer on the game screen."""

    def __init__(self, image, speed):
        """Initialize the powerup object.

            Parameters:
            image (str): Path to the powerup image file.
            speed (int): Movement speed of the powerup.

            Attributes:
            image (pygame.Surface): Scaled powerup image.
            rect (pygame.Rect): Powerup rectangular hitbox.
            speed (int): Powerup movement speed.
            spawnLocationsX (tuple): List of x-coordinates for powerup spawning positions.
            availablePowerUps (tuple): List of available powerup types.
            activation_time (int): Time remaining for the powerup effect."""

        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image), 0.2)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.spawnLocationsX = (210, 315, 420, 525)
        self.availablePowerUps = (Invincibility, Slowing, ChangeCar, Reverse)
        self.activation_time = 0

    def activate(self, player):
        """Activates the powerup effect for the player.

            Parameters:
            player (Player): The game player.

            Returns:
            None"""

        print("Activated")
        self.activation_time = pygame.time.get_ticks()

    def deactivate(self, player):
        """Disables and removes the powerup effect from the player.

            Parameters:
            player (Player): The game player.

            Returns:
            None"""

        print("Deactivated")
        self.repaint()
        player.affected = False
        player.activate = None

    def changeSpeed(self, speed):
        """Updates the powerups movement speed.

            Parameters:
            speed (int): New movement speed.

            Returns:
            None"""

        self.speed = speed

    def powerupMove(self, speed):
        """Moves the powerup object across the screen.

            Parameters:
            speed (int): Multiplier applied to the powerups movement speed.

            Returns:
            None"""

        self.rect.y += self.speed * speed / 20

    def new_mask(self):
        """Creates a new mask object for the powerups image.

           Returns:
            pygame.mask.Mask: The newly created mask object."""

        return pygame.mask.from_surface(self.image)

    def repaint(self, isReverse=False):
        """Repositions the powerup object based on its state and respawns it.

            Parameters:
            isReverse (bool): Whether the powerup is reversing its direction. Defaults to False.

            Returns:
            None"""

        if isReverse:
            self.rect.y = 3000
        else:
            self.rect.y = -3000
        self.rect.x = random.choice(self.spawnLocationsX)

    def draw_countdown(self, screen):
        """Draws the countdown timer on the game screen based on the remaining powerup effect duration.

           Parameters:
            screen (pygame.Surface): The game screen surface.

           Returns:
            None"""

        if self.activation_time > 0:
            time_passed = pygame.time.get_ticks() - self.activation_time
            time_remaining = max(0, 6 * 1000 - time_passed)
            if time_remaining > 0:
                font = pygame.font.Font(None, 40)
                text1 = font.render(f"{time_remaining // 1000}", True, (0, 0, 0))
                text2 = font.render("0", True, (0, 0, 0))
                time = pygame.image.load("time.png")
                time = pygame.transform.scale(time, (250, 200))
                screen.blit(time, (-50, 400))
                screen.blit(text1, (78, 497))
                screen.blit(text2, (58, 497))


class Invincibility(PowerUp):
    """Invincibility powerup class.

        This class represents an invincibility powerup that grants the player immunity to enemy attacks for a limited duration.

        Attributes:
        image (pygame.Surface): Scaled invincibility powerup image.
        rect (pygame.Rect): Invincibility powerup rectangular hitbox.
        speed (int): Movement speed of the powerup.
        spawnLocationsX (tuple): List of x-coordinates for powerup spawning positions.
        availablePowerUps (tuple): List of available powerup types.
        activation_time (int): Time remaining for the invincibility effect.
        duration (int): Duration of invincibility in seconds.

        Methods:
        init(speed): Initializes the invincibility powerup object.
        activates(player, isPlayer2=False): Activates the invincibility effect for the player.
        deactivates(player): Deactivates and removes the invincibility effect from the player."""

    def __init__(self, speed):
        """Initializes the invincibility powerup object.

            Parameters:
            speed (int): Movement speed of the powerup.

            Attributes:
            image (pygame.Surface): Scaled invincibility powerup image.
            rect (pygame.Rect): Invincibility powerup rectangular hitbox.
            speed (int): Movement speed of the powerup.
            spawnLocationsX (tuple): List of x-coordinates for powerup spawning positions.
            availablePowerUps (tuple): List of available powerup types.
            activation_time (int): Time remaining for the invincibility effect.
            duration (int): Duration of invincibility in seconds."""

        super().__init__("powerup.invencibility.png", speed)
        self.duration = 5  # Duration of invincibility in seconds

    def activate(self, player, isPlayer2=False):
        """Activates the invincibility powerup effect for the player.

            Parameters:
            player (Player): The game player.
            isPlayer2 (bool, optional): Whether the player is the second player. Defaults to False.

            Returns:
            None"""

        self.activation_time = pygame.time.get_ticks()
        player.Invencible()
        if isPlayer2:
            pygame.time.set_timer(pygame.USEREVENT + 5, self.duration * 1000, 1)
        else:
            pygame.time.set_timer(pygame.USEREVENT+1, self.duration * 1000, 1)

    def deactivate(self, player):
        """Disables and removes the invincibility powerup effect from the player.

            Parameters:
            player (Player): The game player.

            Returns:
            None"""

        super().deactivate(player)
        player.No_Invencible()


class Slowing(PowerUp):
    """Slowing powerup class.

        A class that represents a slowing powerup, which temporarily slows down player movement.

        Attributes:
        speed (float): The initial speed of the object to slow down.
        duration (int): The duration in seconds for which the powerup affects the player.
        activation_time (int): The timestamp of when the powerup was activated.

        Methods:
        init(self, speed): Initializes the Slowing powerup object.
        activate(self, player, isPlayer2=False): Activates the powerup, affecting the specified player.
        deactivate(self, player): Deactivates the powerup, removing its effects from the player."""

    def __init__(self, speed):
        """Initializes a Slow Powerup object.

        Parameters:
        self (SlowPowerup): The SlowPowerup object to initialize.
        speed (float): The initial speed of the object to slow down."""

        super().__init__("powerup.slow.png", speed)
        self.duration = 5

    def activate(self, player, isPlayer2=False):
        """Activates the powerup, slowing down the player's movement speed.

        Parameters:
        player (Player): The player to affect.
        isPlayer2 (bool, optional): Whether this powerup is for player 2. Defaults to False.

        Returns:
        None"""

        player.Slower()
        main.speed = 0.8
        self.activation_time = pygame.time.get_ticks()
        if isPlayer2:
            pygame.time.set_timer(pygame.USEREVENT + 6, self.duration * 1000, 1)
        else:
            pygame.time.set_timer(pygame.USEREVENT + 2, self.duration * 1000, 1)

    def deactivate(self, player):
        """Deactivates the player.

        This function deactivates the player by calling the parent class's deactivate() method, then removes the Slower effect from the player and sets the global game speed to 1.

        Parameters
        player (Player): The player to deactivate."""

        super().deactivate(player)
        player.No_Slower()
        main.speed = 1


class ChangeCar (PowerUp):
    """ChangeCar class

    This class represents the car change powerup in the racing game. It inherits from the PowerUp class and provides methods for initializing, activating, and deactivating the powerup.

    Attributes:
    image (str): The path to the powerups image
    duration (int): The duration of the powerups effect
    original_model (Model): The player's original model before activating the powerup

    Methods:
    init(speed): Initializes the powerup object with the specified speed and additional attributes
    activate(player, isPlayer2=False): Activates the car change powerup for the specified player
    deactivate(player): Deactivates the specified player, reverting any changes made during activation"""

    def __init__(self, speed):
        """Initializes a powerup object with the specified speed and additional attributes

        Parameters:
        speed (int): The speed of the powerup

        Attributes:
        self.image (str): The path to the powerups image
        self.duration (int): The duration of the powerups effect
        self.original_model (Model): The player's original model before activating the powerup"""

        super().__init__("powerup.change.png", speed)
        self.duration = 5
        self.original_model = None

    def activate(self, player, isPlayer2=False):
        """Activates the car change powerup for the specified player.

        Parameters:
        player (Player): The player object to affect.
        isPlayer2 (bool): Whether the player is the second player (default: False).

        Returns:
        None"""

        print("Change car")
        player.change = True
        player.repaint(True)
        self.activation_time = pygame.time.get_ticks()
        if isPlayer2:
            pygame.time.set_timer(pygame.USEREVENT + 7, self.duration * 1000, 1)
        else:
            pygame.time.set_timer(pygame.USEREVENT + 3, self.duration * 1000, 1)

    def deactivate(self, player):
        """Deactivates the specified player, reverting any changes made during activation.

        Parameters:
        player (Player): The player to be deactivated.

        Returns:
        None"""

        player.change = False
        player.repaint(isPlayer=True, model=self.original_model)
        # Revert any changes made during activation


class Reverse(PowerUp):
    """Reverse powerup class.

    This class represents the reverse powerup that can be picked up by players in the game. When activated, it reverses the game speed for the affected player.

    Attributes:
    duration: The duration of the powerup effect in seconds.

    Methods:
     _init_(self, speed): Initializes the reverse powerup object with the specified speed.
     activate(self, player, isPlayer2=False): Activates the powerup for the specified player.
    deactivate(self, player): Deactivates the powerup for the specified player."""

    def __init__(self, speed):
        """Initializes the reverse powerup object.

        Args:
        speed (int): The initial speed of the powerup."""

        super().__init__("powerup.reverse.png", speed)
        self.duration = 5  # Duration of power-up in seconds

    def activate(self, player, isPlayer2=False):
        """Activates the powerup effect for the specified player.

        Parameters:
        param1 (player): The player object to apply the powerup effect to.
        param2 (isPlayer2=False): Boolean flag indicating whether the player is the second player.

        Returns:
        None"""

        player.Reversible()
        main.speed = -1
        self.activation_time = pygame.time.get_ticks()
        if isPlayer2:
            pygame.time.set_timer(pygame.USEREVENT + 8, self.duration * 1000, 1)
        else:
            pygame.time.set_timer(pygame.USEREVENT + 4, self.duration * 1000, 1)

    def deactivate(self, player):
        """Deactivates a player and sets the game speed to 1.

        Parameters:
        player: The player to be deactivated.

        Returns:
        None"""

        super().deactivate(player)
        player.No_Reversible()
        main.speed = 1
