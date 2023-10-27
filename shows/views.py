from django.shortcuts import render, redirect
from .models import Show, Movie,Category, Profile
# Create your views here.

def moviegenreresults(request):
    if request.method == 'POST':
        genreresult = request.POST['genreresult']
        Category = Show.objects.filter(Genre__contains = genreresult)
        return render(request, 'moviegenreresults.html',
                      {'genreresult': genreresult,
                       'Category': Category})
    else:
        return render(request, 'moviegenreresults.html',
                      {})


def showgenreresults(request):
    if request.method == 'POST':
        genreresult = request.POST['genreresult']
        Category = Show.objects.filter(Genre__contains = genreresult)
        return render(request, 'showgenreresults.html',
                      {'genreresult': genreresult,
                       'Category': Category})
    else:
        return render(request, 'showgenreresults.html',
                      {})


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
def movielist(request):
    movie_list = Movie.objects.all()
    return render(request , 'movielist.html',
    {'movie_list' : movie_list})

def moviemovie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    return render(request , 'moviemovie.html',
    {'movie' : movie} )


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



