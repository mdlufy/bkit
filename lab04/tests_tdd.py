import unittest
from main import client_code
from main import ComputerDeveloper
from main import MobileDeveloper
from unittest.mock import patch



class TestGameCreators(unittest.TestCase):
    def test_computer_developer(self):
        expected_result = "Client: I'm not aware of the creator's class, but it still works." \
                          "\nCreator: Today the company has created a new game: Computer game created"
        actual_result = client_code(ComputerDeveloper())
        self.assertEqual(expected_result, actual_result, "Something is wrong with creating a computer game object")

    def test_mobile_developer(self):
        expected_result = "Client: I'm not aware of the creator's class, but it still works." \
                          "\nCreator: Today the company has created a new game: Mobile game created"
        actual_result = client_code(MobileDeveloper())
        self.assertEqual(expected_result, actual_result, "Something is wrong with creating a mobile game object")


class TestComputerDeveloper(unittest.TestCase):
    @patch('main.ComputerGame.operation', return_value="Computer game created")
    def test_operation(self, operation):
        self.assertEqual(operation(self), "Computer game created")




if __name__ == "__main__":
    unittest.main()