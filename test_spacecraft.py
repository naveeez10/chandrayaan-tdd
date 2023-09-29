import unittest
from spacecraft import *

class SpacecraftTests(unittest.TestCase):
    
    def test_initialization_from_user_input(self):
        """Test initialization of spacecraft with predefined input values."""
        spacecraft, x, y, z, direction = user_input_spacecraft()
        
        self.assertEqual(spacecraft.x, x)
        self.assertEqual(spacecraft.y, y)
        self.assertEqual(spacecraft.z, z)
        self.assertEqual(spacecraft.direction, direction)
    
    def test_move_forward_with_direction_N(self):
        """Test moving forward when the spacecraft is facing North."""
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)        
        spacecraft.move("forward")      
        self.assertEqual(spacecraft.y,1)
        self.assertEqual(spacecraft.direction,"N")
        
    def test_move_backward_with_direction_N(self):
        """Test moving backward when the spacecraft is facing North."""
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        spacecraft.move("backward")       
        self.assertEqual(spacecraft.y,-1)
        self.assertEqual(spacecraft.direction,"N")
        
    def test_turn_right_with_direction_N(self):
        """Test turning right when the spacecraft is facing North."""
        
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        spacecraft.move("turn right")
        self.assertEqual(spacecraft.direction,"E")
        
    def test_turn_left_with_direction_N(self):
        """Test turning left when the spacecraft is facing North."""
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        spacecraft.move("turn left")        
        self.assertEqual(spacecraft.direction,"W")
    
    def test_turn_U_with_direction_N(self):
        """Test turning U when the spacecraft is facing North."""
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        spacecraft.move("turn U")     
        self.assertEqual(spacecraft.direction,"U")
        
    def test_turn_D_with_direction_N(self):
        """Test turning D when the spacecraft is facing North."""
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        
        spacecraft.move("turn D")     
        self.assertEqual(spacecraft.direction,"D")
        
    def test_move_forward_with_direction_S(self):
        """Test moving forward when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("forward",)       
        self.assertEqual(spacecraft.y, -1)
        self.assertEqual(spacecraft.direction, "S")
        
    def test_move_backward_with_direction_S(self):
        """Test moving backward when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("backward")        
        self.assertEqual(spacecraft.y, 1)
        self.assertEqual(spacecraft.direction, "S")
        
    def test_turn_right_with_direction_S(self):
        """Test turning right when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("turn right")
        
        self.assertEqual(spacecraft.direction, "W")
        
    def test_turn_left_with_direction_S(self):
        """Test turning left when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("turn left")
        
        self.assertEqual(spacecraft.direction, "E")
    
    def test_turn_U_with_direction_S(self):
        """Test turning U when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("turn U",)      
        self.assertEqual(spacecraft.direction, "U")
        
    def test_turn_D_with_direction_S(self):
        """Test turning D when the spacecraft is facing South."""
        spacecraft = Spacecraft(direction="S", x=0, y=0, z=0)
        
        spacecraft.move("turn D",)      
        self.assertEqual(spacecraft.direction, "D")
    def test_move_forward_with_direction_E(self):
        """Test moving forward when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("forward",)       
        self.assertEqual(spacecraft.x, 1)
        self.assertEqual(spacecraft.direction, "E")
        
    def test_move_backward_with_direction_E(self):
        """Test moving backward when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("backward")        
        self.assertEqual(spacecraft.x, -1)
        self.assertEqual(spacecraft.direction, "E")
        
    def test_turn_right_with_direction_E(self):
        """Test turning right when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("turn right")
        
        self.assertEqual(spacecraft.direction, "S")
        
    def test_turn_left_with_direction_E(self):
        """Test turning left when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("turn left")
        
        self.assertEqual(spacecraft.direction, "N")
    
    def test_turn_U_with_direction_E(self):
        """Test turning U when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("turn U",)      
        self.assertEqual(spacecraft.direction, "U")
        
    def test_turn_D_with_direction_E(self):
        """Test turning D when the spacecraft is facing East."""
        spacecraft = Spacecraft(direction="E", x=0, y=0, z=0)
        
        spacecraft.move("turn D",)      
        self.assertEqual(spacecraft.direction, "D")

    def test_move_forward_with_direction_W(self):
        """Test moving forward when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("forward",)       
        self.assertEqual(spacecraft.x, -1)
        self.assertEqual(spacecraft.direction, "W")
        
    def test_move_backward_with_direction_W(self):
        """Test moving backward when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("backward")        
        self.assertEqual(spacecraft.x, 1)
        self.assertEqual(spacecraft.direction, "W")
        
    def test_turn_right_with_direction_W(self):
        """Test turning right when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("turn right")
        
        self.assertEqual(spacecraft.direction, "N")
        
    def test_turn_left_with_direction_W(self):
        """Test turning left when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("turn left")
        
        self.assertEqual(spacecraft.direction, "S")
    
    def test_turn_U_with_direction_W(self):
        """Test turning U when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("turn U",)      
        self.assertEqual(spacecraft.direction, "U")
        
    def test_turn_D_with_direction_W(self):
        """Test turning D when the spacecraft is facing West."""
        spacecraft = Spacecraft(direction="W", x=0, y=0, z=0)
        
        spacecraft.move("turn D",)      
        self.assertEqual(spacecraft.direction, "D")

    def test_move_forward_with_direction_U(self):
        """Test moving forward when the spacecraft is facing U."""
        spacecraft = Spacecraft(direction="U", x=0, y=0, z=0)
        
        spacecraft.move("forward",)       
        self.assertEqual(spacecraft.z, 1)
        self.assertEqual(spacecraft.direction, "U")
        
    def test_move_backward_with_direction_U(self):
        """Test moving backward when the spacecraft is facing U."""
        spacecraft = Spacecraft(direction="U", x=0, y=0, z=0)
        
        spacecraft.move("backward")        
        self.assertEqual(spacecraft.z, -1)
        self.assertEqual(spacecraft.direction, "U")
        
    def test_turn_right_with_direction_U(self):
        """Test turning right when the spacecraft is facing U."""
        spacecraft = Spacecraft(direction="U", x=0, y=0, z=0)
        
        spacecraft.move("turn right")
        
        self.assertEqual(spacecraft.direction, "S")
        
    def test_turn_left_with_direction_U(self):
        """Test turning left when the spacecraft is facing U."""
        spacecraft = Spacecraft(direction="U", x=0, y=0, z=0)
        
        spacecraft.move("turn left")
        
        self.assertEqual(spacecraft.direction, "N")
    def test_move_forward_with_direction_DOWN(self):
        """Test moving forward when the spacecraft is facing D."""
        spacecraft = Spacecraft(direction="D", x=0, y=0, z=0)
        
        spacecraft.move("forward",)       
        self.assertEqual(spacecraft.z, -1)
        self.assertEqual(spacecraft.direction, "D")
        
    def test_move_backward_with_direction_DOWN(self):
        """Test moving backward when the spacecraft is facing D."""
        spacecraft = Spacecraft(direction="D", x=0, y=0, z=0)
        
        spacecraft.move("backward")        
        self.assertEqual(spacecraft.z, 1)
        self.assertEqual(spacecraft.direction, "D")
        
    def test_turn_right_with_direction_DOWN(self):
        """Test turning right when the spacecraft is facing D."""
        spacecraft = Spacecraft(direction="D", x=0, y=0, z=0)
        
        spacecraft.move("turn right")
        
        self.assertEqual(spacecraft.direction, "N")
        
    def test_turn_left_with_direction_DOWN(self):
        """Test turning left when the spacecraft is facing D."""
        spacecraft = Spacecraft(direction="D", x=0, y=0, z=0)
        
        spacecraft.move("turn left")
        
        self.assertEqual(spacecraft.direction, "S")
    
    def test_invalid_command(self):
        """Test when invalid commmand is passed."""
        
        spacecraft = Spacecraft(direction='N',x=0,y=0,z=0)
        
        spacecraft.move("hehehe")     
        self.assertEqual(spacecraft.direction,'N')
    
    def test_turn_U_with_direction_U(self):
        spacecraft = Spacecraft(direction='U',x=0,y=0,z=0)
        spacecraft.move("turn U")
        self.assertEqual(spacecraft.direction, 'D')
    
    
    def test_out_of_bounds(self):
            spacecraft = Spacecraft(direction='N',x=0,y=5,z=0)
            spacecraft.move("forward")
            self.assertLessEqual(spacecraft.y,y_bound)
              
if __name__ == '__main__':
    unittest.main()
