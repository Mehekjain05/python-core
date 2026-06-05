# You work on an HR system. Every time an employee marks attendance, the company wants to record:
#
# The employee's action
# The time at which the action occurred
#
# Instead of adding logging code inside every attendance-related function, use a decorator to automatically log the activity.
from unittest import result
from datetime import datetime

def log_activity(fx):

    def inside_func(*args):
        print("Activity Started")
        print(datetime.now())
        result = fx(*args)
        print("Activity Completed")
        return result

    return inside_func

class Employee:
    @log_activity
    def mark_attendance(self, employee_name):
        self.employee_name = employee_name

        print(f"{self.employee_name} marked attendance")

    @log_activity
    def apply_leave(self, employee_name, days):
        self.employee_name = employee_name
        self.days = days

        print(f"Employee : {self.employee_name} is taking a leave of {self.days} days.")


emp1 = Employee()
emp1.mark_attendance("Mehek Jain")
emp1.apply_leave("Mehek Jain", 3)