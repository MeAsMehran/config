from django.contrib import admin

# Register your models here.
from .models import Article

# class ArticleAdmin(admin.AdminSite):
#     pass


admin.site.register(Article)

