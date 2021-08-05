from django.contrib import admin
from rango.models import Category, Movie
from rango.models import UserProfile, Category, User, Movie_rating, Movie_hot


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')


# admin.site.register(Movie, MovieAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Movie_rating)
admin.site.register(Movie_hot)
