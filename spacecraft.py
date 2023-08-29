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
        
    def move(self, distance):
        # Move the spacecraft in its current direction by a specified distance.
        if self.direction == "N":
            self.y += distance
        elif self.direction == "S":
            self.y -= distance
        elif self.direction == "E":
            self.x += distance
        elif self.direction == "W":
            self.x -= distance
        elif self.direction == "UP":
            self.z += distance
        elif self.direction == "DOWN":
            self.z -= distance
        else:
            raise ValueError(f"Invalid movement direction: {self.direction}")
        
    def rotate(self, new_direction):
        # Rotate the spacecraft to a new direction.
        if new_direction not in DIRECTIONS:
            raise ValueError(f"Invalid direction: {new_direction}")
        self.direction = new_direction

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
