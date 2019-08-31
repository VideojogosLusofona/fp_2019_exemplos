# Import pygame into our program
import pygame

# Define a main function, just to keep things nice and tidy
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (640, 360)
    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))
        # Draw primitives
        pygame.draw.rect(screen, (255, 255, 0), (100, 100, 50, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (200, 100, 50, 50), 4)
        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
