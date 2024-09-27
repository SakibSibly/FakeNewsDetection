from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        required=True, 
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        required=True, 
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        required=True, 
        label='Country',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        required=True, 
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
