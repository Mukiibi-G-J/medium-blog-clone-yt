from django.contrib import admin
from .models import  Post, Comments
# <-------------------- first way to add to the admin site----------------------------->
# admin.site.register(Post)
                 
# <-------------------- second way to add to the admin site----------------------------->

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'publish', 'status')
  prepopulated_fields = {'slug':('title',)}
  search_fields =('title', 'body')
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  order_by = ('publish', 'status')

@admin.register(Comments) 
class CommentsAdmin(admin.ModelAdmin):
  list_display =('name',)