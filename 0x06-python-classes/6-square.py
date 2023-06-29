#!/usr/bin/python3

class Square:
    """
    The square to be created and its attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializations of all instances of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter: Gets the size of the square (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the sqaures size
        """
        if type(value) != int:
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter: Gets the exact position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter: Sets the position of the square

        """
        if not type(value) is tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive intergers")
        if not all(type(num) is int and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive intergers")
        self.__position = value

    def area(self):
        """
        Calcs the squares area

        """
        return self.size * self.size

    def my_print(self):
        """
        Code for printing the square with char #
        """
        if self.size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for j in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
