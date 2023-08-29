import unittest
from spacecraft import *

class SpacecraftTests(unittest.TestCase):
    
    def test_initialization_from_user_input(self):
        """Test initialization of spacecraft with predefined input values."""
        # Initialize spacecraft with user input values
        spacecraft, x, y, z, direction = user_input_spacecraft()
        
        # Check if spacecraft's x, y, z, and direction attributes match the user's input
        self.assertEqual(spacecraft.x, x)
        self.assertEqual(spacecraft.y, y)
        self.assertEqual(spacecraft.z, z)
        self.assertEqual(spacecraft.direction, direction.upper())
    
    def test_move_forward_with_direction_N(self):
        """Test moving forward when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Move spacecraft forward by 1 unit
        spacecraft.move("forward",1)
        
        # Assert that spacecraft's y-coordinate has increased by 1 and direction remains North
        self.assertEqual(spacecraft.y,1)
        self.assertEqual(spacecraft.direction,"N")
        
    def test_move_backward_with_direction_N(self):
        """Test moving backward when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Move spacecraft backward by 1 unit
        spacecraft.move("backward",1)
        
        # Assert that spacecraft's y-coordinate has decreased by 1 and direction remains North
        self.assertEqual(spacecraft.y,-1)
        self.assertEqual(spacecraft.direction,"N")
        
    def test_turn_right_with_direction_N(self):
        """Test turning right when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Turn the spacecraft to the right
        spacecraft.move("turn right",0)
        
        # Assert that spacecraft's direction is now East
        self.assertEqual(spacecraft.direction,"E")
        
    def test_turn_left_with_direction_N(self):
        """Test turning left when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Turn the spacecraft to the left
        spacecraft.move("turn left",0)
        
        # Assert that spacecraft's direction is now West (please note that this assertion was incorrect in the original code. "turn left" from "N" should result in "W", not "E".)
        self.assertEqual(spacecraft.direction,"W")
        
    def test_move_forward_with_direction_S(self):
        """Test moving forward when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Move spacecraft forward by 1 unit
        spacecraft.move("forward", 1)
        
        # Assert that spacecraft's y-coordinate has decreased by 1 and direction remains South
        self.assertEqual(spacecraft.y, -1)
        self.assertEqual(spacecraft.direction, "S")
        
    def test_move_backward_with_direction_S(self):
        """Test moving backward when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Move spacecraft backward by 1 unit
        spacecraft.move("backward", 1)
        
        # Assert that spacecraft's y-coordinate has increased by 1 and direction remains South
        self.assertEqual(spacecraft.y, 1)
        self.assertEqual(spacecraft.direction, "S")
        
    def test_turn_right_with_direction_S(self):
        """Test turning right when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Turn the spacecraft to the right
        spacecraft.move("turn right", 0)
        
        # Assert that spacecraft's direction is now West
        self.assertEqual(spacecraft.direction, "W")
        
    def test_turn_left_with_direction_S(self):
        """Test turning left when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Turn the spacecraft to the left
        spacecraft.move("turn left", 0)
        
        # Assert that spacecraft's direction is now East
        self.assertEqual(spacecraft.direction, "E")

        

if __name__ == '__main__':
    unittest.main()
