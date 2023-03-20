from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    """Creates a new snakes and directs it forward"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segments(position)


    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the direction of the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the direction of the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the direction of the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the direction of the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
