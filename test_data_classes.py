import unittest

from unit_tests.data_classes import Person
from unit_tests.data_classes import Employee
from datetime import date

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        p=Person(employee_first_name='John', employee_last_name='Doe')
        self.assertEqual(p.employee_first_name, 'John')
        self.assertEqual(p.employee_last_name, 'Doe')
    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            Person(employee_first_name='J0hn', employee_last_name='D0e')
        with self.assertRaises(ValueError):
            Person(employee_first_name='J@hn', employee_last_name='Doe')
    def test_person_str(self):
        p=Person(employee_first_name='John', employee_last_name='Doe')
        self.assertEqual(str(p), 'John,Doe')

class TestEmployee(unittest.TestCase):
    def test_initialization(self):
        employee = Employee(employee_first_name="John", employee_last_name="Doe", review_date="2023-01-01", review_rating=4)
        self.assertEqual(employee.employee_first_name, "John")
        self.assertEqual(employee.employee_last_name, "Doe")
        self.assertEqual(employee.review_date, date.fromisoformat("2023-01-01"))
        self.assertEqual(employee.review_rating, 4)

    def test_review_date_setter(self):
        employee = Employee(review_date = "2022-12-31")
        #employee.review_date = "2022-12-31"
        self.assertEqual(employee.review_date, date.fromisoformat("2022-12-31"))

       # with self.assertRaises(ValueError):
          #  employee.review_date = "12/31/2022"

    def test_review_rating_setter(self):
        employee = Employee()
        employee.review_rating = 5
        self.assertEqual(employee.review_rating, 5)

        with self.assertRaises(ValueError):
            employee.review_rating = 6

