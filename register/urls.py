from django.urls import path
from . import views

urlpatterns = [
    path("", views.edit_employee, name="employee_insert"),
    path("<int:id>/", views.edit_employee, name="employee_update"),
    path("delete/<int:id>/", views.delete_employee, name="employee_delete"),
    path("employees/", views.get_employee, name="employee_show"),
    path("employees/salary", views.salary_analyse, name="employee_salary")
]
