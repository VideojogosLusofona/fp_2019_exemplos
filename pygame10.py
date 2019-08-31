# Import pygame into our program
import pygame
import pygame.freetype

# Define a main function, just to keep things nice and tidy
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (640, 360)
    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

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
        my_font.render_to(screen, (20, 20), "Hello World!", (255, 255, 0))
        my_font.render_to(screen, (20, 50), "Hello World!", (255, 255, 0), (255, 0, 0))
        my_font.render_to(screen, (20, 80), "Hello World!", (255, 255, 0), None, pygame.freetype.STYLE_OBLIQUE)
        my_font.render_to(screen, (200, 220), "Hello World!", (255, 255, 0), None, pygame.freetype.STYLE_DEFAULT, 90)
        my_font.render_to(screen, (20, 120), "Hello World!", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 100)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
