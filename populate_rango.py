import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Movie

def populate():
    python_movies = [
        {'title': 'Official Python Tutorial',
        'url': 'http://docs.python.org/3/tutorial/', 'movie_likes': '45',},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/', 'movie_likes': '63', },
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/', 'movie_likes': '20', }]

    django_movies = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'movie_likes': '23', },
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/', 'movie_likes': '27', },
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/', 'movie_likes': '14', }]

    other_movies = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/', 'movie_likes': '19', },
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org', 'movie_likes': '13', }]
        
    cats = {
        'Python': {'movies': python_movies, 'movie_likes': 128, 'likes' : 64}, 
        'Django': {'movies': django_movies, 'movie_likes': 64, 'likes': 32},
        'Other Frameworks': {'movies': other_movies, 'movie_likes': 32, 'likes': 16}}

    for cat, cat_data in cats.items():  
        c = add_cat(
            cat, movie_likes=cat_data['movie_likes'], likes=cat_data['likes'])
        for p in cat_data['movies']:
            add_movie(c, p['title'], p['url'], movie_likes=p['movie_likes'])

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_movie(cat, title, url, movie_likes=0): 
    p = Movie.objects.get_or_create(category=cat, title=title)[0] 
    p.url = url 
    p.movie_likes = movie_likes
    p.save()
    return p


def add_cat(name, movie_likes=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0] 
    c.movie_likes = movie_likes
    c.likes = likes
    c.save() 
    return c

# Start execution here!
if __name__ == '__main__': 
    print('Starting Rango population script...') 
    populate()
