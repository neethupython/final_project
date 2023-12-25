from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Department, UserProfile, Course, Material, FormModel  # Import FormModel
from django.contrib.auth.models import User  # Add this line
from .models import FormModel, Material


class UserProfileForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    courses = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = UserProfile
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    # Add any additional fields you need
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class FormModelForm(forms.ModelForm):
    purpose = forms.ChoiceField(
        choices=[('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')],
        widget=forms.Select(attrs={'class': 'form-control-sm'})
    )
    materials_provide = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    # Modify the gender field to use the choices
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control-sm'}))

    class Meta:
        model = FormModel
        exclude = []  # You can exclude any fields if needed


class YourForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
