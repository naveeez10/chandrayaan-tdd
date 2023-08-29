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

if __name__ == '__main__':
    unittest.main()
