import unittest
from spacecraft import *


class SpacecraftTests(unittest.TestCase):

    def test_initialization_from_user_input(self):
        """Test initialization of spacecraft with predefined input values."""
        spacecraft, x, y, z, direction = user_input_spacecraft()
        
        self.assertEqual(spacecraft.x, x)
        self.assertEqual(spacecraft.y, y)
        self.assertEqual(spacecraft.z, z)
        self.assertEqual(spacecraft.direction, direction.upper())
    
    def test_move_in_direction(self):
        # Test the spacecraft's movement based on its direction.
        spacecraft = Spacecraft(direction="N",x=0,y=0,z=0)
        spacecraft.move(5)
        self.assertEqual(spacecraft.y, 5)
        spacecraft.rotate("S")
        spacecraft.move(2)
        self.assertEqual(spacecraft.y, 3)
        spacecraft.rotate("UP")
        self.assertEqual(spacecraft.y,3)

if __name__ == '__main__':
    unittest.main()
