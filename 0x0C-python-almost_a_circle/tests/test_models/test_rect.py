import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Rectangle_Test_Cases(unittest.TestCase):

    def test_rectangle_creation(self):
        """ Test creating a rectangle instance """
        rect = Rectangle(10, 5)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_rectangle_with_id(self):
        """ Test creating a rectangle instance with an explicit id """
        rect = Rectangle(10, 5, 2, 3, 100)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_set_width(self):
        """ Test setting the width attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_height(self):
        """ Test setting the height attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.height = 8
        self.assertEqual(rect.height, 8)

    def test_set_x(self):
        """ Test setting the x-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_set_y(self):
        """ Test setting the y-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.y = 2
        self.assertEqual(rect.y, 2)

    def test_get_width(self):
        """ Test getting the width attribute of a rectangle """
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)

    def test_set_width(self):
        """ Test setting the width attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_width_with_negative_value(self):
        """ Test setting the width attribute with a negative value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_set_width_with_zero_value(self):
        """ Test setting the width attribute with a zero value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_set_width_with_non_integer_value(self):
        """ Test setting the width attribute with a non-integer value """
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.width = 5.5

    def test_get_height(self):
        """ Test getting the height attribute of a rectangle """
        rect = Rectangle(10, 5)
        self.assertEqual(rect.height, 5)

    def test_set_height(self):
        """ Test setting the height attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.height = 8
        self.assertEqual(rect.height, 8)

    def test_set_height_with_negative_value(self):
        """ Test setting the height attribute with a negative value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.height = -5

    def test_set_height_with_zero_value(self):
        """ Test setting the height attribute with a zero value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_set_height_with_non_integer_value(self):
        """ Test setting the height attribute with a non-integer value """
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.height = 5.5

    def test_get_x(self):
        """ Test getting the x-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5, 3, 2)
        self.assertEqual(rect.x, 3)

    def test_set_x(self):
        """ Test setting the x-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.x = 4
        self.assertEqual(rect.x, 4)

    def test_set_x_with_negative_value(self):
        """ Test setting the x-coordinate attribute with a negative value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.x = -2

    def test_set_x_with_non_integer_value(self):
        """ Test setting the x-coordinate
        attribute with a non-integer value """
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.x = 4.5

    def test_get_y(self):
        """ Test getting the y-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5, 3, 2)
        self.assertEqual(rect.y, 2)

    def test_set_y(self):
        """ Test setting the y-coordinate attribute of a rectangle """
        rect = Rectangle(10, 5)
        rect.y = 4
        self.assertEqual(rect.y, 4)

    def test_set_y_with_negative_value(self):
        """ Test setting the y-coordinate attribute with a negative value """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.y = -2

    def test_set_y_with_non_integer_value(self):
        """ Test setting the y-coordinate
        attribute with a non-integer value """
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.y = 4.5

    def test_rectangle_area(self):
        """ Test calculating the area of a rectangle """
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_rectangle_display(self):
        """ Test displaying the rectangle """
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_with_args(self):
        """ Test updating attributes using positional arguments """
        rect = Rectangle(10, 5)
        rect.update(20, 15, 3, 2)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 0)  # y should not be updated

    def test_update_with_kwargs(self):
        """ Test updating attributes using keyword arguments """
        rect = Rectangle(10, 5)
        rect.update(width=15, height=3, x=2)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 0)  # y should not be updated

    def test_update_with_args_and_kwargs(self):
        """ Test updating attributes using
        both positional and keyword arguments """
        rect = Rectangle(10, 5)
        rect.update(20, width=15, height=3, x=2)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 0)  # y should not be updated

    def test_to_dictionary(self):
        """ Test converting a rectangle object to a dictionary """
        rect = Rectangle(10, 5, 2, 3, 100)
        expected_dict = {'id': 100, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
