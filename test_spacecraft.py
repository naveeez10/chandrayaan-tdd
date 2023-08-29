import unittest
from spacecraft import Spacecraft

class SpacecraftTests(unittest.TestCase):

    def test_initialization(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        self.assertEqual(spacecraft.x, 0)
        self.assertEqual(spacecraft.y, 0)
        self.assertEqual(spacecraft.z, 0)
        self.assertEqual(spacecraft.direction, 'N')

if __name__ == '__main__':
    unittest.main()
