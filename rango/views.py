
from datetime import datetime
from rango.bing_search import run_query
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rango.models import Category, Movie,User, Genre, Movie_rating,  Movie_hot
from rango.forms import CategoryForm, MovieForm, CommentForm
from django.contrib import messages
from django.views.generic import  DetailView

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context=context_dict)


def index(request):
    # without '-' will sequence from the most to the least
    category_list = Category.objects.order_by('-likes')[:5]
    movie_list = Movie.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['movies'] = movie_list
    visitor_cookie_handler(request)
    response = render(request, 'rango/index.html', context=context_dict)
    return response


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


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        movies = Movie.objects.filter(category=category)
        context_dict['movies'] = movies
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['movies'] = None
    return render(request, 'rango/category.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango: index'))
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_movie(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = MovieForm(category)
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            if category:
                movie = form.save(commit=False)
                movie.category = category
                movie.views = 0
                movie.save()
                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug':
                                                category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_movie.html', context=context_dict)


# def register(request):
#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = UserProfileForm(request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']

#             profile.save()

#             registered = True
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     return render(request, 'rango/register.html',
#                   context={'user_form': user_form,
#                            'profile_form': profile_form,
#                            'registered': registered})


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('rango:index'))
#             else:
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#             print(f"Invalid login details: {username}, {password}")
#             return HttpResponse("Invalid login details supplied.")

#     else:
#         return render(request, 'rango/login.html')


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse('rango:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(
        request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(
        last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
    return render(request, 'rango/search.html', {'result_list': result_list})

class MovieDetailView(DetailView):
    '''movie detail page'''
    model = Movie
    template_name = 'rango/detail.html'

    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to judge if login
        login = True
        try:
            user_id = self.request.session['user_id']
        except KeyError as e:
            login = False  # not login

        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)

        if login:
            # Get the current user's historical rating data
            user = User.objects.get(pk=user_id)

            rating = Movie_rating.objects.filter(user=user, movie=movie).first()
            # default value
            score = 0
            comment = ''
            if rating:
                score = rating.score
                comment = rating.comment
            context.update({'score': score, 'comment': comment})

        #comments
        Com=Movie_rating.objects.filter(movie=movie,comment__regex='^(a-z|A-Z|0-9)*[^$%^&*;:,<>?()\""\']{1,100}$')
        hot_comments = list(Com)[:6]
        print(hot_comments)
        context.update({'hot_comments': hot_comments})

        return context

    # receive form
    def post(self, request, pk):
        url = request.get_full_path()
        form = CommentForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data.get('score')
            comment = form.cleaned_data.get('comment')
            print(score, comment)
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            movie = Movie.objects.get(pk=pk)

            # Comment update 
            rating = Movie_rating.objects.filter(user=user, movie=movie).first()
            if rating:
                # print(rating)
                rating.score = score
                rating.comment = comment
                rating.save()
                # messages.info(request,"Comment updated successfully!")
            else:
                print('Comment does not exist ')
                rating = Movie_rating(user=user, movie=movie, score=score, comment=comment)
                rating.save()
            messages.info(request, "successful!")

        else:
            # The form is not validated
            messages.info(request, "Rating cannot be empty!")
        return redirect(reverse('rango:detail', args=(pk,)))