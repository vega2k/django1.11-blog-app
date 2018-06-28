from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','count_text']
    list_display_links = ['title']

    def count_text(self,mypost):
        return '{}글자'.format(len(mypost.text))
    
    count_text.short_description = '내용 글자수'

# Register your models here.
admin.site.register(Post,PostAdmin)