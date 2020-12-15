from django.contrib import admin
from web_models import models

# Register your models here.
admin.site.register([models.position, models.gender, models.hero, ])
