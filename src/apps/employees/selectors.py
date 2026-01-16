from .models import Employee

class EmployeeSelector:
    @staticmethod
    def list(filters):
        qs = Employee.objects.all().order_by("-id")

        if filters.get("department"):
            qs = qs.filter(department=filters["department"])

        if filters.get("role"):
            qs = qs.filter(role=filters["role"])

        return qs
