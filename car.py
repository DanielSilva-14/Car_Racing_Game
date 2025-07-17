import pygame
import random


# "Car" class is a subclass of pygame.sprite.Sprite. It can be used as a sprite in a Pygame game.
class Car(pygame.sprite.Sprite):
    """A Car class for a Pygame-based game, representing a car sprite with various attributes and behaviors.

        This class inherits from pygame.sprite.Sprite and provides functionalities for car movement, collision detection, and visual representation in a game.
        It includes methods for moving the car in different directions, checking collisions, bouncing off boundaries, changing speed, and updating visual appearances according to different states like invincibility or slowing down.

        Parameters:
        model (str): The type of car model to use.
        width (int): The width of the car sprite.
        height (int): The height of the car sprite.
        speed (int): The initial speed of the car.

        Attributes:
        width (int): The current width of the car sprite.
        height (int): The current height of the car sprite.
        speed (int): The current speed of the car.
        model (str): The type of car model.
        original_model (str): The original car model without any modifications.
        invincible (bool): Whether the car is invincible, making it temporarily immune to collisions.
        slowing (bool): Whether the car is currently slowing down.
        change (bool): Whether the car model is currently changing.
        reverse (bool): Whether the car is driving in reverse.
        image (pygame.Surface): The scaled car image.
        rect (pygame.Rect): The rectangle object representing the car's position and size."""

    def __init__(self, model, width, height, speed):
        """Initializes a car object based on specified parameters.

        Parameters:
        model (str): The type of car model to use.
        width (int): The width of the car sprite.
        height (int): The height of the car sprite.
        speed (int): The initial speed of the car.

        Attributes:
        width (int): The current width of the car sprite.
        height (int): The current height of the car sprite.
        speed (int): The current speed of the car.
        model (str): The type of car model.
        original_model (str): The original car model without any modifications.
        invincible (bool): Whether the car is invincible, making it temporarily immune to collisions.
        slowing (bool): Whether the car is currently slowing down.
        change (bool): Whether the car model is currently changing.
        reverse (bool): Whether the car is driving in reverse.
        image (pygame.Surface): The scaled car image.
        rect (pygame.Rect): The rectangle object representing the car's position and size."""

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Initialise attributes of the car
        self.width = width
        self.height = height
        self.speed = speed
        self.model = model
        self.original_model = model
        self.activePowerup = None

        # Next flags might be used for game logic to track specific states of the car.
        self.invincible = False

        self.slowing = False

        self.change = False

        self.reverse = False

        # This line loads an image of the car based on its model and convert_alpha() is used to handle transparency in the image.
        car_image = pygame.image.load(f"car.{model}.png").convert_alpha()

        # loaded image to the specified width while maintaining its aspect ratio. It uses pygame.transform.scale_by() for the scaling.
        self.image = pygame.transform.scale_by(car_image, width/car_image.get_width())

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def collision(self, collision_area, x=0, y=0):
        """Checks for collision between the car and a specified collision area.

        Parameters:
        collision_area (pygame.mask.Mask): The collision area to check against.
        x (int): X-axis offset for adjusting the car's position.
        y (int): Y-axis offset for adjusting the car's position.

        Returns:
        bool: True if the car collides with the specified collision area, False otherwise."""

        car_collision_area = pygame.mask.from_surface(self.image)
        position_adjustment = (int(self.rect.x - x), int(self.rect.y - y))
        intersection = collision_area.overlap(car_collision_area, position_adjustment)
        return intersection

    def bounce(self, border_mask):
        """Implements a horizontal bounce effect for the car when it collides with border.

        Parameters:
        border_mask (pygame.mask.Mask): The mask representing the game's boundaries."""

        self.speed -= 0.05
        if self.rect.x < 800/2:
            self.moveRight(7)
        else:
            self.moveLeft(7)

    def bounce_vertical(self):
        """Implements a vertical bounce effect for the car when it collides with border.
        This ensures that the car bounces off the border and maintains a vertical movement pattern while also applying a slight deceleration effect."""

        self.speed -= 0.05
        if self.rect.y > 600/2:
            self.moveForward(7)
        else:
            self.moveBackward(7)

    def new_mask(self):
        """Generates a new mask for the car's current image.
        This function utilizes the `pygame.mask.from_surface()` method to create a new mask representation of the car's image.
        This mask is crucial for collision detection, as it allows for accurate detection of interactions between the car and other objects in the game environment.

        Returns:
        pygame.mask.Mask: A new mask object representing the car's current image."""

        return pygame.mask.from_surface(self.image)

    def moveRight(self, pixels):
        """Updates the car's position by moving it rightward by a specified number of pixels.

        Parameters:
        pixels (int): The number of pixels to move the car to the right.

        This function modifies the car's x-coordinate in its rectangle object (`self.rect.x`) by adding the specified number of pixels. This effectively moves the car to the right on the screen."""

        self.rect.x += pixels

    def moveLeft(self, pixels):
        """Updates the car's position by moving it leftward by a specified number of pixels.

        Parameters:
        pixels (int): The number of pixels to move the car to the left.

        This function modifies the car's x-coordinate in its rectangle object (`self.rect.x`) by subtracting the specified number of pixels. This effectively moves the car to the left on the screen."""

        self.rect.x -= pixels

    def moveForward(self, pixels):
        """Updates the car's position by moving it forward by a specified number of pixels.

        Parameters:
        pixels (int): The number of pixels to move the car forward.

        In the context of a driving game, this function would be used to move the car forward, navigating the virtual roads and obstacles."""
        
        self.rect.y -= pixels

    def moveBackward(self, pixels):
        """Updates the car's position by moving it backward by a specified number of pixels.

        Parameters:
        pixels (int): The number of pixels to move the car backward.

        In the context of a driving game, this function would be used to move the car backward, navigating the virtual roads and obstacles."""

        self.rect.y += pixels

    def trafficMove(self, speed):
        """Moves the car based on its speed and adjusts its position accordingly.

        Parameters:
        speed (int): The speed of the car."""

        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        """Modifies the car's current speed to the specified value.

        Parameters:
        speed (int): The new speed value for the car.

        This function updates the car's speed attribute (`self.speed`) to the provided value. This change can be used to accelerate, decelerate, or maintain the car's current speed."""

        self.speed = speed

    def repaint(self, isPlayer=False, model=None):
        """Reloads and rescales the car's image to reflect the specified model or the player's choice if the `isPlayer` flag is set.

        Parameters:
        isPlayer (bool, optional): A flag indicating whether the car is controlled by a player. Default value is False.
        model (str, optional): The desired car model to use. If not provided, the current model is maintained.

        This function plays a crucial role in maintaining the visual appearance of the car based on the player's choice or the game's logic.
        It allows for different car models to be used without affecting the car's movement or behavior."""

        if isPlayer:
            # reloads and rescales the car's image, repainting it
            model_list = ["yellow", "branco", "azul", "purpleplayer", "vermelho"]
        else:
            model_list = ["purple", "red", "green", "blue"]
        if model:
            self.model = model
            car_image = pygame.image.load(f"car.{self.model}.png").convert_alpha()
            self.image = pygame.transform.scale_by(car_image, self.width / car_image.get_width())

        else:
            self.model = random.choice([model for model in model_list if model != self.model])
            car_image = pygame.image.load(f"car.{self.model}.png").convert_alpha()
            self.image = pygame.transform.scale_by(car_image, self.width / car_image.get_width())

    def reverse(self):
        """Reverses the car's direction by negating its current speed.

        This function modifies the car's `speed` attribute to its absolute value multiplied by -1. This effectively reverses the car's movement direction without changing its speed value.

        The `reverse()` function is useful for enabling the car to move backward in the game environment. It allows the car to change directions and navigate in reverse if necessary."""
        self.speed = -self.speed

    def Invencible(self):
        """Enables the hero's invincible mode.

        This function sets the `invincible` flag to `True`.
        It also copies the current hero's model to a temporary variable (`original_model`) for restoring it later.
        Additionally, it loads a special invincible hero image from "hero.png" and applies a scale transformation to adjust its size to 100x100 pixels.

        Parameters:
        None

        Returns:
        None"""

        self.invincible = True
        hero_image = pygame.image.load("hero.png").convert_alpha()
        self.image = pygame.transform.scale(hero_image, (100,100))

    def No_Invencible(self):
        """Disables the hero's invincible mode and reverts to the original model.

        This function resets the `invincible` flag to `False`.
        It also restores the model to the value stored in the `original_model` variable.
        Additionally, it loads the original image from the file "car.{model}.png" and scales it proportionally to fit the current width.

        Parameters:
        None

        Returns:
        None"""

        self.invincible = False
        self.model = self.original_model
        car_image = pygame.image.load(f"car.{self.model}.png").convert_alpha()
        self.image = pygame.transform.scale_by(car_image, self.width / car_image.get_width())

    def Slower(self):
        """Activates the slower mode, represented by a turtle image.

        This function sets the `slowing` flag to `True`.
        It also copies the current model to a temporary variable (`original_model`) for restoration later.
        Additionally, it loads a turtle image from "tartaruga.png" and scales it to a size of 100x100 pixels, reflecting the slowed movement.

        Parameters:
        None

        Returns:
        None"""

        self.slowing = True
        turtle_image = pygame.image.load("tartaruga.png").convert_alpha()
        self.image = pygame.transform.scale(turtle_image, (100, 100))

    def No_Slower(self):
        """Deactivates the slower mode and reverts to the original speed.

        This function resets the `slowing` flag to `False`.
        It also restores the model to the value stored in the `original_model` variable.
        Additionally, it loads the original image from the file "car.{model}.png" and scales it proportionally to fit the current width.

        Parameters:
        None

        Returns:
        None"""

        self.slowing = False
        self.model = self.original_model
        car_image = pygame.image.load(f"car.{self.model}.png").convert_alpha()
        self.image = pygame.transform.scale_by(car_image, self.width / car_image.get_width())

    def Reversible(self):
        """Enables the reverse mode, represented by a police car image.

        This function sets the `reverse` flag to `True`.
        It also copies the current model to a temporary variable (`original_model`) for restoration later.
        Additionally, it loads a police car image from "police.png" and scales it proportionally to fit the current width.

        Parameters:
        None

        Returns:
        None"""

        self.reverse = True
        police_image = pygame.image.load("police.png").convert_alpha()
        self.image = pygame.transform.scale_by(police_image, self.width / police_image.get_width())

    def No_Reversible(self):
        """Disables the reverse mode and reverts to the original mode.

        This function resets the `reverse` flag to `False`.
        It also restores the model to the value stored in the `original_model` variable.
        Additionally, it loads the  original image from the file "car.{model}.png" and scales it proportionally to fit the current width.

        Parameters:
        None

        Returns:
        None"""

        self.reverse = False
        self.model = self.original_model
        car_image = pygame.image.load(f"car.{self.model}.png").convert_alpha()
        self.image = pygame.transform.scale_by(car_image, self.width / car_image.get_width())

