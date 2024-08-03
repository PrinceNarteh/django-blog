from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'content', 'published_date']
  list_display_links = ['id', 'title']
  list_filter = ['published_date']
  search_fields = ['title']