from django.shortcuts import render, redirect
from .forms import StudentForm, EmployeeForm, TransactionForm, ContactForm
from .models import Student, Employee, Transaction
from django.db.models import Sum
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm



def homepage(request):
    return render(request, 'homepage.html')

def student_list(request):
    students = Student.objects.all()
    query = request.GET.get('q')
    if query:
        students = students.filter(first_name__icontains=query)
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()
    income = transactions.filter(transaction_type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = transactions.filter(transaction_type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expense
    return render(request, 'transaction_list.html', {
        'transactions': transactions,
        'balance': balance
    })

def offered_courses(request):
    return render(request, 'offered_courses.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success_page.html': True})
        else:
            return JsonResponse({'': False, 'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def privacy(request):
    return render(request, 'privacy_policy.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success_page')  # Redirect to success page
        else:
            # Handle invalid form or authentication failure
            return render(request, 'success_page.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'success_page.html', {'form': form})

def success_page(request):
    if request.user.is_authenticated:
        return render(request, 'success_page.html')
    else:
        return redirect('Login') 


