from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

# 커스텀 User 모델 등록 (기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력안됨)
admin.site.register(User, UserAdmin)