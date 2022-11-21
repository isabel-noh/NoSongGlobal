from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'nickname', 'profile_image', 'like_ost_genre']


# 커스텀 User 모델 등록 (기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력안됨)
admin.site.register(User, UserAdmin)
# UserAdmin.fieldsets += ("Custom fields", {"fields": "name"})

# class UserAdmin(admin.ModelAdmin):"nickname", "profile_image", "like_ost_genre",

#   # username 은 장고에서 제공하는 User 모델에 있는 컬럼명
#   # 관리자 페이지에서 리스트를 보여줄 때 열로 활용
#   list_display = ('username', 'email', 'A', 'B')
#   list_filter = ('username',)