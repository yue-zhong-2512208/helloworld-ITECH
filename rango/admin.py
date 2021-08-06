from django.contrib import admin
from rango.models import Category, Movie, Comment, UserProfile, LikeMovie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(LikeMovie)