    #!/usr/bin/python3
"""Student class module."""


class Student:
    """Student class that defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of the student's attributes.
        """
        return self.__dict__
