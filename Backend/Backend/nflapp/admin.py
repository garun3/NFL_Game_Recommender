from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Game
from .models import Link

admin.site.register(Game)
admin.site.register(Link)