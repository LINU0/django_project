from django import forms
from . import models
from django.forms.widgets import DateTimeInput
# from django.contrib.admin import widgets
#from captcha.fields import CaptchaField

class ProfileForm(forms.ModelForm):
	class Meta:
		model = models.Resident
		fields = ['phone_number','address','emergencycontact',"emergencynumber"]
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['phone_number'].label = '連絡電話'
		self.fields['address'].label = '戶籍地'
		self.fields['emergencycontact'].label = '緊急聯絡人'
		self.fields['emergencynumber'].label = '緊急聯絡電話'

class LoginForm(forms.Form):
    user_name = forms.CharField(label='name:',max_length=30)
    password = forms.CharField(label='password',max_length=20,widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    class Meta:
    	model = models.Book
    	fields = ["name","phone","time","message"]
    	widget={
    	    'time':DateInput(),
    	    }
    def __init__(self,*args,**kwargs):
        super(BookForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = '姓名'
        self.fields['phone'].label = '電話'
        self.fields['time'].label = '預約時間(西元年-月-日 時:分)'
        self.fields['message'].label = '留言'
        # self.fields['time'].widget = widgets.AdminTimeWidget()

class PhotoForm(forms.ModelForm):
	class Meta:
		model = models.Photo
		fields = ['roomnumber','photo']
	def __init__(self, *args, **kwargs):
		super(PhotoForm, self).__init__(*args, **kwargs)
		self.fields['roomnumber'].label = '房號'
		self.fields['photo'].label = '圖片'


