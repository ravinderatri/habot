from .models import Employee

class EmployeeService:

    @staticmethod
    def create_employee(data):
        return Employee.objects.create(**data)

    @staticmethod
    def update_employee(employee, data):
        for key, value in data.items():
            setattr(employee, key, value)
        employee.save()
        return employee

    @staticmethod
    def delete_employee(employee):
        employee.delete()
