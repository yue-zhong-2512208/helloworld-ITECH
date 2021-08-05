from django.contrib.auth.models import User
from rango.models import UserProfile, Movie, Category, Movie_rating
from django import forms


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter the catergory name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=Movie.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(
        max_length=200, help_text="Please enter the URL of the page.")
    movie_likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

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


class CommentForm(forms.ModelForm):
    # check if rate is 0
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        score = cleaned_data.get('score')
        if score == 0:
            raise forms.ValidationError(message='Rate cannot be 0!')
        else:
            return cleaned_data

    class Meta:
        # record score and comment
        model = Movie_rating
        fields = ['score', 'comment']
