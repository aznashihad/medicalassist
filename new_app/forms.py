from django.contrib.auth.forms import UserCreationForm
from django import forms

from new_app.models import Login, Customer, Company, CustomerDonations, Notifications, Feedback


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=('username','password1','password2',)
class CustomerRegister(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=('user',)
class CompanyRegister(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'
        exclude=('user',)




class  CustomerDonationForm(forms.ModelForm):
    class Meta:
        model =  CustomerDonations
        fields = '__all__'
        exclude=('company_approved','admin_approved','rejected',)


# class NotificationForm(forms.ModelForm):
#     class Meta:
#         model = Notification
#         fields = ['message']
#
#
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('feedback',)

class ReplayeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('replay',)