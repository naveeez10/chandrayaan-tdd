class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction.upper()
        self.validate()

    def validate(self):
        if self.direction not in ['N', 'S', 'E', 'W']:
            raise ValueError("Invalid direction!")
        
    def move_x(self,x):
        """Move the spacecraft in the x-direction by the given distance."""
        self.x += x
        
    def move_y(self,y):
        """Move the spacecraft in the y-direction by the given distance."""
        self.y += y
        
    def move_z(self,z):
        """Move the spacecraft in the z-direction by the given distance."""
        self.z += z

def user_input_spacecraft(x=None, y=None, z=None, direction=None):
    """Function to get user input or use predefined values for testing."""
    if x is None:
        x = int(input("Enter x-coordinate: "))
    if y is None:
        y = int(input("Enter y-coordinate: "))
    if z is None:
        z = int(input("Enter z-coordinate: "))
    if direction is None:
        direction = input("Enter direction (N/S/E/W): ")

    return Spacecraft(x, y, z, direction), x, y, z, direction
