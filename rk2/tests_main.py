import unittest
from main import first_task
from main import second_task
from main import third_task



class TestFirstTask(unittest.TestCase):
    def test_value_count(self):
        expected_result = 5
        actual_result = len(first_task())
        self.assertEqual(expected_result, actual_result, "The expected number of employees differs from the actual one")



class TestSecondTask(unittest.TestCase):
    def test_sort_by_max(self):
        expected_result = '311'
        actual_result = str(second_task()[0][1]) + str(second_task()[1][1]) + str(second_task()[1][1])
        self.assertEqual(expected_result, actual_result, "Something went wrong with the sorting")



class TestThirdTask(unittest.TestCase):
    def test_name_end(self):
        count = 0
        for el in list(third_task()):
            if str(el).endswith('ов'):
                count += 1
        actual_result = count
        expected_result = 2
        self.assertEqual(expected_result, actual_result, "Check the endings of words")



if __name__ == "__main__":
    unittest.main()