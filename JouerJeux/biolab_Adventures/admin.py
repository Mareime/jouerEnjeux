from django.contrib import admin
from .models import User,Question,UserQuestion

# Register your models here.
admin.site.register(User)
admin.site.register(UserQuestion)
admin.site.register(Question)

