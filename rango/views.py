#weihan
from datetime import datetime
from rango.bing_search import run_query
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from rango.models import Category, Movie, Comment
from rango.forms import CategoryForm, MovieForm, CommentForm
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse


# for showing about.html
def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context=context_dict)

# for showing index.html
def index(request):
    # without '-' will sequence from the least to the most
    movie_list_byViews = Movie.objects.order_by('-views')[:4]
    movie_list_byLikes = Movie.objects.order_by('-likes')[:4]
    context_dict = {}
    context_dict['boldmessage'] = 'Enjoy your journey in the world of movies.'
    context_dict['moviesByViews'] = movie_list_byViews
    context_dict['moviesByLikes'] = movie_list_byLikes
    visitor_cookie_handler(request)
    response = render(request, 'rango/index.html', context=context_dict)
    return response


# cookie related class
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


# for showing category.html
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        movies = Movie.objects.filter(
            category=category).order_by('-likes')
        context_dict['movies'] = movies
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['movies'] = None
	# Start search functionality code.
    if request.method == 'POST':
        if request.method == 'POST':
            query = request.POST['query'].strip()

            if query:
                context_dict['result_list'] = run_query(query)
                context_dict['query'] = query
    return render(request, 'rango/category.html', context=context_dict)


# for showing movie detail page
def show_movie(request, movie_title_slug):
    context_dict = {}
    try:
        movie = Movie.objects.get(slug=movie_title_slug)
        comments = Comment.objects.filter(movie=movie)
        context_dict['movie'] = movie
        context_dict['comments'] = comments

    except Category.DoesNotExist:
        context_dict['movie'] = None
        context_dict['comments'] = None
    
    # Record views of the page of movies.
    movie.readpage()
    movie.save()
    return render(request, 'rango/movie.html', context=context_dict)


# for showing movie library
def all_movies(request):
    allMovies = Movie.objects.all().order_by('-views')
    context_dict = {}
    context_dict['all_movies'] = allMovies

    return render(request, 'rango/all_movies.html', context=context_dict)


# for adding new category, only for logged users
@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


# for adding new comment, only for logged users
# comment shall slug with the user who wrote it
@login_required
def add_comment(request, movie_title_slug):
    try:
        movie = Movie.objects.get(slug=movie_title_slug)
    except:
        movie = None

    if movie is None:
        return redirect(reverse('rango:index'))

    user = User.objects.get(username=request.user)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if movie:
                comment = form.save(commit=False)
                comment.movie = movie
                comment.user = user
                comment.save()
                return redirect(reverse('rango:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
            else:
                print(form.errors)

    context_dict = {'form': form, 'movie': movie}
    return render(request, 'rango/add_comment.html', context=context_dict)


# for adding new movie, only for logged users
@login_required
def add_movie(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            if category:
                movie = form.save(commit=False)
                movie.category = category
                movie.save()
                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug':
                                                category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_movie.html', context=context_dict)


# for showing a sample restricted page, only for logged users
@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


# Search in the Internet
def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
    return render(request, 'rango/search.html', {'result_list': result_list})


# Search inside the website
def search_insite(request):
    # this function is for get the movie list
    movie_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            movie_list = Movie.objects.filter(title__contains=query)

    return render(request, 'rango/search_insite.html', {'movie_list': movie_list})


# this class is for counting likes
class LikeMovie(View):
    @method_decorator(login_required())
    def get(self, request):
        movie_id = request.GET['movie_id']

        try:
            movie = Movie.objects.get(id=int(movie_id))
        except Movie.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        movie.likes = movie.likes + 1
        movie.save()

        return HttpResponse(movie.likes)
