from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Avg


# class Category(models.Model):
#     NAME_MAX_LENGTH = 128
#     name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     slug = models.SlugField(unique=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name_plural = 'categories'

#     # __str__() = toString()
#     def __str__(self):
#         return self.name


class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    # __str__() = toString()
    def __str__(self):
       return self.name

# class Movie(models.Model):
#     TITLE_MAX_LENGTH = 128
#     URL_MAX_LENGTH = 200
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=TITLE_MAX_LENGTH)
#     url = models.URLField()
#     movie_likes = models.IntegerField(default=0)

#     def likeMovie(self):
#         self.movie_likes += 1
#         return

#     def __str__(self):
#         return self.title


class Movie(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    #category = models.ForeignKey(Category,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    url = models.URLField()
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)

    # 电影名
    name = models.CharField(max_length=256)
    # imdb_id是info文件里面的电影顺序
    imdb_id = models.IntegerField()

    # 时长
    time = models.CharField(max_length=256, blank=True)
    # 类型
    category = models.ManyToManyField(Category)
    # 发行时间
    release_time = models.CharField(max_length=256, blank=True)
    # 简介
    intro = models.TextField(blank=True)
    # 导演
    director = models.CharField(max_length=256, blank=True)
    # 编剧
    writers = models.CharField(max_length=256, blank=True)
    # 演员
    actors = models.CharField(max_length=512, blank=True)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f"<Movie:{self.name},{self.imdb_id}>"

    def get_score(self):
        # 定义一个获取平均分的方法，模板中直接调用即可
        # 格式 {'score__avg': 3.125}
        result_dct = self.movie_rating_set.aggregate(Avg('score'))
        try:
            # 只保留一位小数
            result = round(result_dct['score__avg'], 1)
        except TypeError:
            return 0
        else:
            return result

    def get_user_score(self, user):
        return self.movie_rating_set.filter(user=user).values('score')

    def get_score_int_range(self):
        return range(int(self.get_score()))

    def get_category(self):
        category_dct = self.category.all().values('name')
        category_lst = []
        for dct in category_dct.values():
            category_lst.append(dct['name'])
        return category_lst


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    rating_movies = models.ManyToManyField(Movie, through="Movie_rating")

    def __str__(self):
        return "<USER:( name: {:},password: {:},email: {:} )>".format(self.name, self.password, self.email)


class Movie_rating(models.Model):
    # 评分的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    # 评分的电影
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, unique=False)
    # 分数
    score = models.FloatField()
    # 评论，可选
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Movie_rating'

    class Meta:
        db_table = 'User'


class Movie_hot(models.Model):
    '''存放最热门的一百部电影'''
    # 电影外键
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 评分人数
    rating_number = models.IntegerField()

    class Meta:
        db_table = 'Movie_hot'
        ordering = ['-rating_number']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
