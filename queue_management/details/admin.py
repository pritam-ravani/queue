from django.contrib import admin
from details.models import Category, Sub_Category
# Register your models here.

admin.site.register([Category, Sub_Category])
