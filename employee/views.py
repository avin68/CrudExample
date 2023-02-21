from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from employee.forms import EmployeeForm, SearchForm
from employee.models import Employee


def show(request):
    employees = Employee.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            key = form.cleaned_data['search']
            employees = employees.filter(Q(ename__icontains=key) | Q(efamily__icontains=key))
            return render(request, 'employee/show.html', {'employees': employees, 'form': form})
    return render(request, 'employee/show.html', {'employees': employees, 'form': form})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'employee/edit.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('show')


def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form = EmployeeForm
    return render(request, 'employee/index.html', {'form': form})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request,'employee/edit.html', {'employee':employee})

