from django.contrib import admin
from .models import Movie, Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "description", "date_released")
    inlines = [CommentInline]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
