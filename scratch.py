import arcade
import random
import timeit

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shapes! Non-buffered"

RECT_WIDTH = 50
RECT_HEIGHT = 50

NUMBER_OF_SHAPES = 2

class Shape:
    """ Generic base shape class """
    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_angle = delta_angle
        self.color = color

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.angle += self.delta_angle
        if self.x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if self.y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if self.x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if self.y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1

class Rectangle(Shape):

    def draw(self):
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height,
                                     self.color, 1, self.angle)
class Ellipse(Shape):

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color, self.angle)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None

#        self.processing_time = 0
#        self.draw_time = 0
#        self.frame_count = 0
#        self.fps_start_timer = None
        self.fps = None


    def setup(self):
        """ Set up the game and initialize the variables. """
        self.shape_list = []

        x = random.randrange(0, SCREEN_WIDTH)
        y = random.randrange(0, SCREEN_HEIGHT)
        #width = random.randrange(10, 30)
        width = 100
        #height = random.randrange(10, 30)
        height = 100
        d_x = random.randrange(-3, 4)
        d_y = random.randrange(-3, 4)
        angle = random.randrange(0, 360)
        #d_angle = random.randrange(-3, 4)
        d_angle

        shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                                           d_angle, (255, 255, 255,255))    
        self.shape_list.append(shape)


    def on_update(self, dt):
        """ Move everything """
        for shape in self.shape_list:
            shape.move()


    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for shape in self.shape_list:
            shape.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


