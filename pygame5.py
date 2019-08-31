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
        pygame.draw.line(screen, (255, 0, 0), (50, 300), (200, 150), 1)
        pygame.draw.line(screen, (255, 0, 0), (50, 280), (200, 130), 4)
        pygame.draw.lines(screen, (255, 0, 0), True, [(250, 50), (300, 100), (250, 100)], 1)
        pygame.draw.lines(screen, (255, 0, 0), False, [(350, 50), (400, 100), (350, 100)], 4)
        pygame.draw.aaline(screen, (255, 0, 0), (50, 260), (200, 110), 0)
        pygame.draw.aaline(screen, (255, 0, 0), (50, 240), (200,  90), 1)
        pygame.draw.aalines(screen, (255, 0, 0), True, [(250, 150), (300, 200), (250, 200)], 0)
        pygame.draw.aalines(screen, (255, 0, 0), False, [(350, 150), (400, 200), (350, 200)], 1)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
