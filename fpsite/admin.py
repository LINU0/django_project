from django.contrib import admin
from fpsite import models
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
	list_display = ('name', 'identity')

admin.site.register(models.Account, AccountAdmin)
class RoomAdmin(admin.ModelAdmin):
	list_display = ('roomnumber', 'rent', 'enable', 'detail')

admin.site.register(models.Room, RoomAdmin)
class ResidentAdmin(admin.ModelAdmin):
	list_display = ('name', 'roomnumber', 'enable')

admin.site.register(models.Resident, ResidentAdmin)
class BookAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'time', 'message')

admin.site.register(models.Book, BookAdmin)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'roomnumber', 'email', 'message')

admin.site.register(models.Question,QuestionAdmin)
# class QuestionAdmin(admin.ModelAdmin):
# 	list_display = ( 'roomnumber', 'last_bill', 'current_bill')
admin.site.register(models.Photo)
admin.site.register(models.Electricity_total)
admin.site.register(models.Electricity_personal)
