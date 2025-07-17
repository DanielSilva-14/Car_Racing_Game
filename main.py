from interface import *  # The * symbol is a wildcard that means "import everything."
global speed


def main():
    """Serves as the main entry point for the script, initiating the gameplay process.
    This function acts as the starting point of the application, initiating the overall gameplay process. It calls the `interface()` function, which handles the user interface and game logic.

    This function serves as the central hub for orchestrating the entire game process, initiating the user interface, handling events, and ensuring a smooth gameplay experience.

    Returns:
    None: The function does not directly return a value but initiates the main gameplay loop."""

    interface()  # calls the interface function.


if __name__ == '__main__':  # checks whether the script is being run as the main program
    main()  # calls the main function
