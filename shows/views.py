from django.shortcuts import render, redirect
from .models import Show, Movie,Category, Profile
# Create your views here.

def moviegenreresults(request, category_id):
    movies = Movie.objects.filter(Genre=category_id)
    return render(request, 'moviegenreresults.html', {'movies': movies})

def showgenreresults(request, category_id):
    shows = Show.objects.filter(Genre=category_id)
    return render(request, 'showgenreresults.html', {'shows': shows})


def searchResults(request):
    if request.method == 'POST':
        result = request.POST ['result']
        show = Show.objects.filter(Name__contains = result)
        return render(request, 'searchResults.html',
                      {'result': result,
                       'show' : show})
    else:
        return render(request, 'searchResults.html',
                      {})


def showshow(request, show_id):
    show = Show.objects.get(pk = show_id)
    return render(request , 'showshow.html',
    {'show' : show})

def showlist(request):
    show_list = Show.objects.all()
    return render(request , 'showlist.html',
    {'show_list' : show_list})

def genrelist(request):
    Category_list = Category.objects.all()
    return render(request , 'showgenrelist.html',
    {'Category_list' : Category_list})
def moviegenrelist(request):
    Category_list = Category.objects.all()
    return render(request , 'moviegenrelist.html',
    {'Category_list' : Category_list})
def movielist(request):
    movie_list = Movie.objects.all()
    return render(request , 'movielist.html',
    {'movie_list' : movie_list})

def moviemovie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    Category_list = Category.objects.all()
    return render(request , 'moviemovie.html',
    {'movie' : movie,'Category_list' : Category_list} )


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'profile.html', {'profile': profile} )
    else:
        return redirect('home')


def profilelist(request):
    profiles = Profile.objects.all()
    return render(request , 'profilelist.html',
    {'profiles' : profiles})



