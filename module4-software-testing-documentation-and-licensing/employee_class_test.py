import unittest
from class_example import Employee, Teacher

class EmployeeTest(unittest.TestCase):

    def test_name(self):
        employee_test1 = Employee('Test', 'User', 60, 20)
        self.assertEqual(employee_test1.fullname(), 'Test User')

    def test_salary(self):
        employee_test2 = Employee('Amanda', 'Knox', 20, 35)
        self.assertEqual(employee_test2.salary(), 52*20*35)

    def test_generate_employee_report(self):
        employee_test3 = Teacher('Sally', 'Ride', 70, 50, 'DS5')
        self.assertTrue("Sally.Ride@lambda.com" in employee_test3.generate_employee_report())

if __name__ == '__main__':
    unittest.main()