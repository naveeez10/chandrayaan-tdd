DIRECTIONS = ["N", "S", "E", "W", "UP", "DOWN"]
class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction.upper()
        self.validate()

    def validate(self):
        if self.direction not in DIRECTIONS:
            raise ValueError("Invalid direction!")
        
    def move(self, command, distance):
        """
        Move the spacecraft based on the provided command and distance.

        Args:
            command (str): The movement command. Options are 'forward', 'backward', 'turn left', 
                           'turn right', 'turn up', 'turn down'.
            distance (int, optional): The distance to move. Defaults to 1.
        """
        if command == 'forward':
            self._move_forward(distance)
        elif command == 'backward':
            self._move_backward(distance)
        elif command == 'turn left':
            self._turn_left()
        elif command == 'turn right':
            self._turn_right()
        elif command == 'turn up':
            self._turn_up()
        elif command == 'turn down':
            self._turn_down()

    def _move_forward(self, distance):
        if self.direction == 'N':
            self.y += distance
        elif self.direction == 'S':
            self.y -= distance
        elif self.direction == 'E':
            self.x += distance
        elif self.direction == 'W':
            self.x -= distance
        elif self.direction == 'Up':
            self.z += distance
        elif self.direction == 'Down':
            self.z -= distance

    def _move_backward(self, distance):
        self._move_forward(-distance)

    def _turn_left(self):
        directions_horizontal = ['N', 'E', 'S', 'W']
        if self.direction in directions_horizontal:
            curr_idx = directions_horizontal.index(self.direction)
            self.direction = directions_horizontal[(curr_idx - 1) % 4]

    def _turn_right(self):
        directions_horizontal = ['N', 'E', 'S', 'W']
        if self.direction in directions_horizontal:
            curr_idx = directions_horizontal.index(self.direction)
            self.direction = directions_horizontal[(curr_idx + 1) % 4]

    def _turn_up(self):
        if self.direction not in ['Up', 'Down']:
            self.direction = 'Up'

    def _turn_down(self):
        if self.direction not in ['Up', 'Down']:
            self.direction = 'Down'

def user_input_spacecraft(x=None, y=None, z=None, direction=None):
    """Function to get user input or use predefined values for testing."""
    if x is None:
        x = int(input("Enter x-coordinate: "))
    if y is None:
        y = int(input("Enter y-coordinate: "))
    if z is None:
        z = int(input("Enter z-coordinate: "))
    if direction is None:
        direction = input("Enter direction (UP/DOWN/LEFT/RIGHT/FORWARD/BACKWARD): ").upper()

    return Spacecraft(x, y, z, direction), x, y, z, direction
