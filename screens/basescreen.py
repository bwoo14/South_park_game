import pygame


class BaseScreen:
    """Base class for all game screens"""

    def __init__(self, window):
        # window surface
        self.window = window
        # By default, there is no next screen (= game quits)
        self.next_screen = False
        self.chosen_character = None
        self.game_over = False

    def run(self):
        """
        This is the main method of the class.
        It manages the event loop, and:
        * ticks the clock at 60 FPS
        * calls `update` and `draw`
        * calls `manage_event` for each event received
        * quits the game if the quit button is clicked, or the Escape key is pressed
        """

        clock = pygame.time.Clock()
        
        self.running = True
        while self.running:
            # Tick the clock
            clock.tick(60)
            # Do whatever is needed to update the screen objects
            # self.update()
            # Draw the objects on the screen
            self.draw()
            # Update the display
            pygame.display.update()

            # Event loop
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False

                # Call the manage_event method
                self.manage_event(event)
                if self.next_screen:
                    self.running = False

    @property
    def rect(self):
        """Useful property to check for boundaries and dimensions"""

        return self.window.get_rect()

    def draw(self):
        """Child classes should override this method"""

        print("You should override the DRAW method in your class...")

    def update(self):
        """Child classes should override this method"""

        print("You should override the UPDATE method in your class...")

    def manage_event(self, event):
        """Child classes should override this method"""

        print("You should override the MANAGE_EVENT method in your class...")
