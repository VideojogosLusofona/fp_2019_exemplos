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

    image = pygame.image.load("galad.png")
    focus = pygame.image.load("focus.png")

    x = 200
    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))
        
        # Draw primitives
        screen.blit(image, (x, 50))

        for i in range(0, 20):
            screen.blit(focus, (i * 128, 50), None, pygame.BLEND_ADD)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        x = x - 0.25
        if (x < -128):
            x = 640


# Run the main function
main()
