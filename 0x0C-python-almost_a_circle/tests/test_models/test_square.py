import unittest
from models.square import Square


class Square_Test_Cases(unittest.TestCase):

    def test_square_creation(self):
        """ Test creating a square instance """
        square = Square(5)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_with_id(self):
        """ Test creating a square instance with an explicit id """
        square = Square(5, 2, 3, 100)
        self.assertEqual(square.id, 100)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_set_size(self):
        """ Test setting the size attribute of a square """
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_set_x(self):
        """ Test setting the x-coordinate attribute of a square """
        square = Square(5)
        square.x = 3
        self.assertEqual(square.x, 3)

    def test_set_y(self):
        """ Test setting the y-coordinate attribute of a square """
        square = Square(5)
        square.y = 2
        self.assertEqual(square.y, 2)

    def test_square_str(self):
        """ Test the string representation of a square """
        square = Square(5, 2, 3, 100)
        expected_output = "[Square] (100) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_get_size(self):
        """ Test getting the size attribute of a square """
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_set_size(self):
        """ Test setting the size attribute of a square """
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update_with_args(self):
        """ Test updating attributes using positional arguments """
        square = Square(5)
        square.update(20, 8, 2, 3)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        """ Test updating attributes using keyword arguments """
        square = Square(5)
        square.update(size=8, x=2, y=3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_args_and_kwargs(self):
        """ Test updating attributes using
        both positional and keyword arguments """
        square = Square(5)
        square.update(20, size=8, x=2, y=3)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)


if __name__ == '__main__':
    unittest.main()
