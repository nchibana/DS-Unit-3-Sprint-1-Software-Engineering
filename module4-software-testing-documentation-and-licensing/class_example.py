class Employee:

    """General class to represent employees of Lambda school"""
    
    def __init__(self, first, last, hourly_wage, weekly_hours):
        self.first = first
        self.last = last
        self.company = 'lambda'
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours
        self.email = first + '.' + last + '@' + self.company + '.com'

    def fullname(self):

        """Generate employee's full name"""

        return '{} {}'.format(self.first, self.last)

    def salary(self):

        """Generate employee's yearly salary"""

        return 52 * self.weekly_hours * self.hourly_wage

    def generate_employee_report(self):

        """Generate employee's report"""

        s = Employee.fullname(self) + '\n'
        if self.company is not None:
            s += 'Company:   %s\n' % self.company
        if self.email is not None:
            s += 'Email:  %s\n' % self.email
        if self.hourly_wage is not None:
            s += 'Hourly Wage:   %s\n' % self.hourly_wage
        if self.weekly_hours is not None:
            s += 'Weekly Hours:  %s\n' % self.weekly_hours
        if self.hourly_wage is not None:
            s += 'Salary:   %s\n' % Employee.salary(self)
        return s

class Teacher(Employee):

    """Class to represent specific employees, in this case teachers"""

    def __init__(self, first, last, hourly_wage, weekly_hours, cohort):
        super().__init__(first, last, hourly_wage, weekly_hours)
        self.cohort = cohort


employee_1 = Employee('Michael', 'Lee', 30, 40)
print(employee_1.generate_employee_report())

teacher_1 = Teacher('Rachel', 'Adams', 60, 30, 'CS1')
print(teacher_1.generate_employee_report())