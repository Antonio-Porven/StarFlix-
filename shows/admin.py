from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Show, Movie,Profile, Showrating, Movierating
# Register your models here.


admin.site.register(Show)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Showrating)
admin.site.register(Movierating)
#admin.site.register(Profile)

admin.site.unregister(User)
class ProfileInLine(admin.StackedInline):
    model = Profile
class Useradmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'password', 'email']
    inlines = [ProfileInLine]


admin.site.register(User, Useradmin)