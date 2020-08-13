import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('Galileo', 'Galilei', 1000000)
        emp_2 = Employee('Albert', 'Einstein', 10000000)

        self.assertEqual(emp_1.email, 'Galileo.Galilei@email.com')
        self.assertEqual(emp_2.email, 'Albert.Einstein@email.com')

        emp_1.first_name = "Vincenzo"
        emp_2.first_name = "Elsa"

        self.assertEqual(emp_1.email, 'Vincenzo.Galilei@email.com')
        self.assertEqual(emp_2.email, 'Elsa.Einstein@email.com')

    def test_fullname(self):
        emp_1 = Employee('Galileo', 'Galilei', 1000000)
        emp_2 = Employee('Albert', 'Einstein', 10000000)

        self.assertEqual(emp_1.fullname, 'Galileo Galilei')
        self.assertEqual(emp_2.fullname, 'Albert Einstein')

        emp_1.first_name = "Vincenzo"
        emp_2.first_name = "Elsa"

        self.assertEqual(emp_1.fullname, 'Vincenzo Galilei')
        self.assertEqual(emp_2.fullname, 'Elsa Einstein')

    def test_apply_raise(self):
        emp_1 = Employee('Galileo', 'Galilei', 1000000)
        emp_2 = Employee('Albert', 'Einstein', 10000000)

        emp_1.apply_raise()
        emp_2.apply_raise()
        
        self.assertEqual(emp_1.salary, 1050000)
        self.assertEqual(emp_2.salary, 10500000)

if __name__ == '__main__':
    unittest.main()