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
        
        # Assert that spacecraft's direction is now West 
        self.assertEqual(spacecraft.direction,"W")
    
    def test_turn_up_with_direction_N(self):
        """Test turning Up when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Move spacecraft Up by 1 unit
        spacecraft.move("turn up",0)
        
        # Assert that spacecraft's direction is now Up 
        self.assertEqual(spacecraft.direction,"Up")
        
    def test_turn_down_with_direction_N(self):
        """Test turning down when the spacecraft is facing North."""
        # Initialize spacecraft facing North at position (0, 0, 0)
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        # Move spacecraft down by 1 unit
        spacecraft.move("turn down",0)
        
        # Assert that spacecraft's direction is now Down 
        self.assertEqual(spacecraft.direction,"Down")
        
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
    
    def test_turn_up_with_direction_S(self):
        """Test turning Up when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Turn the spacecraft up
        spacecraft.move("turn up", 0)
        
        # Assert that spacecraft's direction is now Up 
        self.assertEqual(spacecraft.direction, "Up")
        
    def test_turn_down_with_direction_S(self):
        """Test turning down when the spacecraft is facing South."""
        # Initialize spacecraft facing South at position (0, 0, 0)
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        # Turn the spacecraft down
        spacecraft.move("turn down", 0)
        
        # Assert that spacecraft's direction is now Down 
        self.assertEqual(spacecraft.direction, "Down")
        # Tests for direction E (East)
    def test_move_forward_with_direction_E(self):
        """Test moving forward when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Move spacecraft forward by 1 unit
        spacecraft.move("forward", 1)
        
        # Assert that spacecraft's x-coordinate has increased by 1 and direction remains East
        self.assertEqual(spacecraft.x, 1)
        self.assertEqual(spacecraft.direction, "E")
        
    def test_move_backward_with_direction_E(self):
        """Test moving backward when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Move spacecraft backward by 1 unit
        spacecraft.move("backward", 1)
        
        # Assert that spacecraft's x-coordinate has decreased by 1 and direction remains East
        self.assertEqual(spacecraft.x, -1)
        self.assertEqual(spacecraft.direction, "E")
        
    def test_turn_right_with_direction_E(self):
        """Test turning right when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Turn the spacecraft to the right
        spacecraft.move("turn right", 0)
        
        # Assert that spacecraft's direction is now South
        self.assertEqual(spacecraft.direction, "S")
        
    def test_turn_left_with_direction_E(self):
        """Test turning left when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Turn the spacecraft to the left
        spacecraft.move("turn left", 0)
        
        # Assert that spacecraft's direction is now North 
        self.assertEqual(spacecraft.direction, "N")
    
    def test_turn_up_with_direction_E(self):
        """Test turning Up when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Turn the spacecraft up
        spacecraft.move("turn up", 0)
        
        # Assert that spacecraft's direction is now Up 
        self.assertEqual(spacecraft.direction, "UP")
        
    def test_turn_down_with_direction_E(self):
        """Test turning down when the spacecraft is facing East."""
        # Initialize spacecraft facing East at position (0, 0, 0)
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        # Turn the spacecraft down
        spacecraft.move("turn down", 0)
        
        # Assert that spacecraft's direction is now Down 
        self.assertEqual(spacecraft.direction, "DOWN")


    # Tests for direction W (West)
    def test_move_forward_with_direction_W(self):
        """Test moving forward when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Move spacecraft forward by 1 unit
        spacecraft.move("forward", 1)
        
        # Assert that spacecraft's x-coordinate has decreased by 1 and direction remains West
        self.assertEqual(spacecraft.x, -1)
        self.assertEqual(spacecraft.direction, "W")
        
    def test_move_backward_with_direction_W(self):
        """Test moving backward when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Move spacecraft backward by 1 unit
        spacecraft.move("backward", 1)
        
        # Assert that spacecraft's x-coordinate has increased by 1 and direction remains West
        self.assertEqual(spacecraft.x, 1)
        self.assertEqual(spacecraft.direction, "W")
        
    def test_turn_right_with_direction_W(self):
        """Test turning right when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Turn the spacecraft to the right
        spacecraft.move("turn right", 0)
        
        # Assert that spacecraft's direction is now North
        self.assertEqual(spacecraft.direction, "N")
        
    def test_turn_left_with_direction_W(self):
        """Test turning left when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Turn the spacecraft to the left
        spacecraft.move("turn left", 0)
        
        # Assert that spacecraft's direction is now South 
        self.assertEqual(spacecraft.direction, "S")
    
    def test_turn_up_with_direction_W(self):
        """Test turning Up when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Turn the spacecraft up
        spacecraft.move("turn up", 0)
        
        # Assert that spacecraft's direction is now Up 
        self.assertEqual(spacecraft.direction, "UP")
        
    def test_turn_down_with_direction_W(self):
        """Test turning down when the spacecraft is facing West."""
        # Initialize spacecraft facing West at position (0, 0, 0)
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        # Turn the spacecraft down
        spacecraft.move("turn down", 0)
        
        # Assert that spacecraft's direction is now Down 
        self.assertEqual(spacecraft.direction, "DOWN")



        

if __name__ == '__main__':
    unittest.main()
