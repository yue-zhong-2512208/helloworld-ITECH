from django.contrib.auth.models import User
from rango.models import UserProfile, Movie, Category, Comment
from django import forms
from django.utils import timezone

# form for add_category
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter the catergory name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

# form for add_movie
class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=Movie.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of your movie.")
    url = forms.URLField(
        max_length=200, help_text="Please enter the URL of your movie.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    poster = forms.ImageField(
        help_text="Please upload the poster of your movie.", required=False)
    story = forms.CharField(
        help_text="Please enter the main story of your movie.")
    year = forms.IntegerField(
        help_text="Please enter the production year of your movie.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    posternum = forms.IntegerField(widget=forms.HiddenInput(), initial=50)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


# form for add comment
class CommentForm(forms.ModelForm):
    comments = forms.CharField(
        max_length=128, widget=forms.Textarea, help_text="Please ennter the coomment content.")
    time = forms.DateTimeField(
        widget=forms.HiddenInput(), initial=timezone.now)

    class Meta:
        model = Comment
        exclude = ('movie', 'user', )
