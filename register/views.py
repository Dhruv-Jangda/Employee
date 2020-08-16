from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def get_employee(request):
    context = {"employees": Employee.objects.all()}
    return render(request, "register/employees.html", context=context)


def salary_analyse(request):
    employees = Employee.objects.all()
    context = {"position": [], "salary": []}
    for idx in range(len(employees)):
        context["position"].append(str(employees[idx].position))
        context["salary"].append(employees[idx].salary)
    # context = {
    #     "position": list(Employee.objects.values_list("position", flat=True)),
    #     # "position" will only have ids & not details
    #     "salary": list(Employee.objects.values_list("salary", flat=True))
    # }
    return render(request, "register/salary_chart.html", context=context)


def edit_employee(request, id=0):
    if request.method == "GET":
        if id == 0:
            emp_form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            emp_form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html",
                      {"emp_form": emp_form})
    else:
        if id == 0:
            emp_form = EmployeeForm(request.POST)  # Insert Opeartion
        else:
            employee = Employee.objects.get(pk=id)
            emp_form = EmployeeForm(
                request.POST, instance=employee)  # Update Operation
        if emp_form.is_valid():
            emp_form.save()
        return redirect("/employee/employees")


def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/employees")
