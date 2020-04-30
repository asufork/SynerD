from django import forms
from django.forms import ModelForm
from .models import UserInfo

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'firstname', 'middle', 'lastname', 'address1', 'address2', 'city', 'state', 'zipcode', 'email', 'homephone', 'cell', 'dobday']	
        exclude = ['dobmonth', 'dobyear', 'employername', 'employeraddress1', 'employeraddress2', 'employercity', 'employerzip', 'employerphone', 'jobtitle', 'governmentIDtype', 'governmentIDnumber', 'governmentIDissuecountry','governmentIDexpiredate', 'governmentIDissue','governmentIDissuestate', 'beneficiaryID']
