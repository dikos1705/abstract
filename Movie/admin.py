from django.contrib import admin
from .models import *
# Register your models here.
from actors.models import Actors

class FilmModelAdmin(admin.ModelAdmin):
    def render_change_form(self,request, context,*args, **kwargs):
        context['adminform'].form.fields['actors'].queryset =Actors.objects.filter(is_star = True) 
        return super().render_change_form(request, context, *args,**kwargs)

admin.site.register(Film)
admin.site.register(Commercial,FilmModelAdmin)