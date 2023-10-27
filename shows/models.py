from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

# Create your models here.




class Category(models.Model):
    id = models.AutoField(primary_key= True)
    Genre = models.CharField('Genres', max_length=120)

    def __str__(self):
        return self.Genre


class Show(models.Model):
    id = models.AutoField(primary_key= True)
    Name = models.CharField('Show Name', max_length= 120)
    number_ep = models.CharField('Number of Episodes', max_length= 120)
    summary = models.TextField('Show Summary', blank=True)
    Genre = models.ManyToManyField(Category)
    Cover_Image = models.ImageField(null = True , upload_to= "images/ShowCovers/", max_length= 2000)
    youtubeVideoKey = models.CharField('Youtube trailer video id', max_length=20000, null = True)
    average_rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.Name

    def Avgrating(self):
        avg_rating = self.showrating_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return avg_rating

class Showrating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __int__(self):
        return self.rating


class Movie(models.Model):
    id = models.AutoField(primary_key= True)
    Name = models.CharField('Movie Name', max_length= 120)
    Runtime = models.CharField('Runtime(min)', max_length= 120)
    summary = models.TextField('Movie Summary', blank=True)
    Genre = models.ManyToManyField(Category)
    Cover_Image = models.ImageField(null = True , upload_to= "images/MovieCovers/", max_length= 2000)
    youtubeVideoKey = models.CharField('Youtube trailer video id', max_length=20000, null = True)
    average_rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.Name

    def Avgrating(self):
        avg_rating = self.movierating_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return avg_rating

class Movierating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __int__(self):
        return self.rating


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_Image= models.ImageField('Profile Picture', null=True, upload_to="images/",
                                    max_length=2000, blank=True, default='images/ProfileImage.png')
    Bio = models.CharField('Bio', max_length=120000, blank=True)
    watching = models.ManyToManyField(Show)
    backgroundcolor = models.CharField('backgroundcolor', max_length=120000, default='black')

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile,sender = User)

def show_genre_results(request, category_id):
    # Retrieve the category and associated shows
    category = Category.objects.get(id=category_id)
    shows = category.show_set.all()

    context = {
        'category': category,
        'shows': shows,
    }

    return render(request, 'showgenreresults.html', context)

def home(request):
    # Assuming Show.objects.all() returns all shows in your database
    all_shows = Show.objects.all()
    random_shows = sample(list(all_shows), 3)  # Adjust '3' to the number of shows you want to display
    return render(request, 'homepage.html')






