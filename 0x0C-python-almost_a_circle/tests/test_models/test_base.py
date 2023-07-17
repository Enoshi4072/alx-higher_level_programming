import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
from unittest import TestCase
from unittest.mock import patch, mock_open
from unittest.mock import mock_open, MagicMock


class Base_Test_Cases(unittest.TestCase):

    def setUp(self):
        """ Reset the counter before the method """
        Base._Base__nb_objects = 0

    def test_automatic_id_generation(self):
        """ Test to determine if an id is automattically generated """
        inst1 = Base()
        inst2 = Base()
        self.assertEqual(inst1.id, 1)
        self.assertEqual(inst2.id, 2)

    def test_when_id_is_provided(self):
        """ If the id is assigned correctly when it is provided """
        inst1 = Base(id=15)
        self.assertEqual(inst1.id, 15)

    def test_when_negative_id(self):
        """ If a negative id is provided """
        inst1 = Base(id=-20)
        self.assertEqual(inst1.id, -20)

    def test_when_id_are_provided_and_auto_gen(self):
        """ when an id isprovided and when auto gen """
        inst1 = Base()
        inst2 = Base(14)
        inst3 = Base()
        self.assertEqual(inst1.id, 1)
        self.assertEqual(inst2.id, 14)
        self.assertEqual(inst3.id, 2)

    def test_when_none(self):
        """ When none is ptovided """
        inst1 = Base(None)
        inst2 = Base(None)
        self.assertEqual(inst1.id, 1)
        self.assertEqual(inst2.id, 2)

    def test_to_json_string(self):
        """ When a string is given """
        list_dict = [{'id': 1, 'name': 'inst1'}, {'id': 2, 'name': 'inst2'}]
        result = json.dumps(list_dict)
        self.assertEqual(Base.to_json_string(list_dict), result)

    def test_an_empty_list(self):
        """ When an empty list id provided """
        list_dict = []
        result = "[]"
        self.assertEqual(Base.to_json_string(list_dict), result)

    def test_when_none_is_give(self):
        """ When None is provided as the input """
        list_dict = None
        result = "[]"
        self.assertEqual(Base.to_json_string(list_dict), result)

    def test_save_to_file(self):
        """ Test saving objects to a file """
        # Create instances of Base subclasses
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        square1 = Square(5)
        square2 = Square(4)
        # Call save_to_file method
        with patch('builtins.open', mock_open()) as mock_file:
            Base.save_to_file([rect1, rect2, square1, square2])
            # Check if the file was opened and written correctly
            mock_file.assert_called_once_with('Base.json', 'w')
            mock_file().write.assert_called_once_with('[{"id": 1, "width": 10, "heght": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "heght": 3, "x": 0, "y": 0}, {"id": 3, "width": 5, "heght": 5, "x": 0, "y": 0}, {"id": 4, "width": 4, "heght": 4, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """ Test converting a JSON string to a list of dictionaries """
        json_string = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 3, "x": 0, "y": 0}]'
        expected_result = [{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 3, "x": 0, "y": 0}]

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_result)

    def test_from_json_string_with_empty_string(self):
        """ Test converting an empty JSON string """
        json_string = ''
        expected_result = '[]'

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_result)

    def test_from_json_string_with_none(self):
        """ Test converting a None JSON string """
        json_string = None
        expected_result = '[]'

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_result)

    def test_create_rectangle(self):
        """ Test creating a Rectangle instance using the create method """
        dictionary = {'id': 1, 'width': 5, 'height': 3, 'x': 0, 'y': 0}
        rectangle = Rectangle.create(**dictionary)

        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_create_square(self):
        """ Test creating a Square instance using the create method """
        dictionary = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        square = Square.create(**dictionary)

        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_create_with_invalid_class_name(self):
        """ Test creating an instance with an invalid class name """
        dictionary = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        instance = Base.create(**dictionary)

        self.assertIsNone(instance)

    def test_load_from_file_rectangle(self):
        """ Test loading a list of Rectangle instances from a file """
        mock_data = '[{"id": 1, "width": 5, "height": 3, "x": 0, "y": 0}]'

        mock_open_func = MagicMock(return_value=mock_open(read_data=mock_data).return_value)
        with unittest.mock.patch('builtins.open', mock_open_func):
            rectangles = Rectangle.load_from_file()

        self.assertEqual(len(rectangles), 1)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 5)
        self.assertEqual(rectangles[0].height, 3)
        self.assertEqual(rectangles[0].x, 0)
        self.assertEqual(rectangles[0].y, 0)

    def test_load_from_file_file_not_found(self):
        """ Test loading from a file that does not exist """
        mock_open_func = MagicMock(side_effect=FileNotFoundError)
        with unittest.mock.patch('builtins.open', mock_open_func):
            rectangles = Rectangle.load_from_file()

        self.assertEqual(len(rectangles), 0)

if __name__ == '__main__':
    unittest.main()
