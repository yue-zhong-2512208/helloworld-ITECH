from django.contrib import admin
from rango.models import Category, Movie, Comment
from rango.models import UserProfile


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Movie, MovieAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Comment)
admin.site.register(UserProfile)
