from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def add_employee_view(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    template_name = 'emp_app/employee_form.html'
    context = {'form':form}
    return render(request, template_name, context)


def show_employee_view(request):
    objs = Employee.objects.all()
    template_name = 'emp_app/employee_show.html'
    context  = {'objs':objs}
    return render(request, template_name, context)


def update_employee_view(request, pk):
    objs = Employee.objects.get(id=pk)
    form = EmployeeForm(instance = objs)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=objs)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'emp_app/employee_update.html'
    context = {'form':form}
    return render(request, template_name, context)
    #return HttpResponse(f'<h1>PK VALUE IS: {pk}</h1>')

def delete_employee_view(request, pk):
    objs = Employee.objects.get(id=pk)
    objs.delete()
    return redirect('show_url')
    #return HttpResponse(f'<h1> PK VALUE IS:{pk}</h1>')