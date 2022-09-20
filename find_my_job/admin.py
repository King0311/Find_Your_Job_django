from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(hr_profile)
admin.site.register(seeker_profile)
admin.site.site_header = "Find_my_job"
admin.site.site_title = "Find_your_job"
admin.site.site_index = "Find my job"