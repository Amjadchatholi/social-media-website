from django.contrib import admin
from . models import Vote, Reaction

# Register your models here.
admin.site.register(Vote)
admin.site.register(Reaction)