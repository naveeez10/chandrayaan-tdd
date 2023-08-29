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
    
    def test_move_x(self):
        # Test movement in the x-direction.
        spacecraft = Spacecraft(5,5,5,'E')
        spacecraft.move_x(2)
        self.assertEqual(spacecraft.x, 7)
    
    def test_move_y(self):
        # Test movement in the y-direction
        spacecraft = Spacecraft(5,5,5,'E')
        spacecraft.move_y(2)
        self.assertEqual(spacecraft.y, 8)
        
    def test_move_z(self):
        # Test Movement in the z-direction
        spacecraft = Spacecraft(5,5,5,'E')
        spacecraft.move_z(2)
        self.assertEqual(spacecraft.z, 7)

if __name__ == '__main__':
    unittest.main()
