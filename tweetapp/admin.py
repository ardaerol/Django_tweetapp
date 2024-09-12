from django.contrib import admin
from . import models
# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname Group',{"fields":["nickname"]}),
        ('Message Group',{"fields":["message"]})
    ]
    #fields = ['message']
#bu class admin özelleştirme adminin görebileceği kontrolleri kısıtlama gibi

admin.site.register(models.Tweet,TweetAdmin)