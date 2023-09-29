from typing import Tuple

DIRECTIONS = ["N", "S", "E", "W", "U", "D"]
y_bound = 5
class Spacecraft:
    def __init__(self, x:int, y:int, z:int, direction: str) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction.upper()

        self.DIRECTION_MATRIX = {
            'N': {'x': 0, 'y': 1, 'z': 0},
            'E': {'x': 1, 'y': 0, 'z': 0},
            'S': {'x': 0, 'y': -1, 'z': 0},
            'W': {'x': -1, 'y': 0, 'z': 0},
            'U': {'x': 0, 'y': 0, 'z': 1},
            'D': {'x': 0, 'y': 0, 'z': -1}
        }

        self.Directions = ["N", "E", "S", "W"]
        
        

    def move(self, command):
        if command == 'forward':
            self.go(1)
        elif command == 'backward':
            self.go(-1)
        elif command == 'turn left':
            self.turn(-1) 
        elif command == 'turn right':
            self.turn(1)  
        elif command == 'turn U':
            if self.direction == 'U':
                self.direction = 'D'
            else:
                self.direction = 'U'
        elif command == 'turn D':
            self.direction = 'D'
        else:
            print("Invalid Commandd")

    def turn(self, turn_direction):
        if self.direction == 'U':
            self.direction = 'S' if turn_direction == 1 else 'N'
            return

        if self.direction == 'D':
            self.direction = 'N' if turn_direction == 1 else 'S'
            return

        current_idx = self.Directions.index(self.direction)
        new_idx = (current_idx + turn_direction + 4) % 4
        self.direction = self.Directions[new_idx]

    def go(self, step):
        direction_values = self.DIRECTION_MATRIX.get(self.direction)
        if not direction_values:
            raise ValueError(f"Invalid direction: {self.direction}")

        # The variable step's value can be 1 or -1, indicating whether to go forward for backwards
        self.x += direction_values['x'] * step
        self.y += direction_values['y'] * step
        if(self.y > y_bound):
            self.y = y_bound
        self.z += direction_values['z'] * step

def user_input_spacecraft(x=None, y=None, z=None, direction=None) -> Tuple[Spacecraft, int, int, int, str]:
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