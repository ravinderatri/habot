from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema

from .models import Employee
from .serializers import EmployeeSerializer
from .services import EmployeeService
from .selectors import EmployeeSelector


class EmployeePagination(PageNumberPagination):
    page_size = 10


class EmployeeListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=EmployeeSerializer,
        responses=EmployeeSerializer,
    )
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = EmployeeService.create_employee(serializer.validated_data)
        return Response(
            EmployeeSerializer(employee).data,
            status=status.HTTP_201_CREATED
        )



class EmployeeDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return Response(EmployeeSerializer(employee).data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = EmployeeService.update_employee(
            employee, serializer.validated_data
        )
        return Response(EmployeeSerializer(employee).data)

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        EmployeeService.delete_employee(employee)
        return Response(status=status.HTTP_204_NO_CONTENT)
