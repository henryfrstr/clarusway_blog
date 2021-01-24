# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile
# from django.contrib.auth.forms import PasswordResetForm


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError(
#                 'Please use another Email, that is already taken')
#         return email


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ('username', 'email')


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image', 'bio']


# # class EmailValidationOnForgotPassword(PasswordResetForm):

# #     def clean_email(self):
# #         email = self.cleaned_data['email']
# #         if not User.objects.filter(email__iexact=email, is_active=True).exists():
# #             msg = ("There is no user registered with the specified E-Mail address.")
# #             self.add_error('email', msg)
# #         return email
