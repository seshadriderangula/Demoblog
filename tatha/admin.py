from django.contrib import admin
from .models import Student,Contact,Register,Send

# Register your models here.

admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Send)

