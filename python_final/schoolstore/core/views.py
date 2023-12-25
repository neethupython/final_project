from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, FormModelForm, YourForm
from django.contrib.auth import login, authenticate
from .models import Department
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse


def home(request):
    # Get the list of all departments
    departments = Department.objects.all()

    context = {
        'departments': departments,
    }

    return render(request, 'home.html', context)


def department_wikipedia(request, department_id):
    # Assuming you have a Department model with a Wikipedia URL field
    try:
        department = Department.objects.get(pk=department_id)
        # Redirect to the department's Wikipedia URL
        return HttpResponseRedirect(department.wikipedia_link)
    except Department.DoesNotExist:
        # Handle the case where the department is not found
        return render(request, 'department_not_found.html')


@login_required
def new_page(request):
    if request.method == 'POST':
        form = FormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed')
            return redirect('home')
    else:
        form = FormModelForm()
    return render(request, 'new_page.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def get_courses(request):
    department_id = request.GET.get('department_id')

    # Fetch courses based on the selected department
    courses = Course.objects.filter(department_id=department_id)

    # Create a list of dictionaries for rendering options in the template
    courses_data = [{'id': course.id, 'name': course.name} for course in courses]

    return HttpResponse(courses_data, content_type='application/json')


def your_view(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
        return render(request, 'home.html', {'message': 'Order Confirmed'})
        # Set success message


    else:
        form = YourForm()

    return render(request, 'new_page.html', {'form': form})
