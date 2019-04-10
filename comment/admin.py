from django.contrib import admin
from .models import  Comments




class CommentsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]



    class Meta:
        model = Comments

admin.site.register(Comments, CommentsAdmin)
