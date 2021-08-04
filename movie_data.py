import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
import csv
import time
import os.path
from django.contrib import messages
from django.db.models import Avg, Count, Max
from django.http import HttpResponse, request
from rango.forms import  CommentForm
from django.views.generic import View, ListView, DetailView
from rango.models import User, Movie, Genre, Movie_rating
BASE = os.path.dirname(os.path.abspath(__file__))
'''!!! 导入csv文件用'''
def get_genre():
    '''导入所有电影类型'''
    path=os.path.join(BASE,'rango\static\movie\info\genre.txt')
    with open(path) as fb:
        for line in fb:
            Genre.objects.create(name=line.strip())

def get_movie_info():
    '''导入所有电影信息，设置它们的类型'''
    path=os.path.join(BASE,'rango\static\movie\info\info.csv')
    with open(path) as fb:
        reader=csv.reader(fb)
        title=reader.__next__()
        # 读取title信息 id,name,url,time,genre,release_time,intro,directores,writers,starts
        # 这里的id是imbd的id，根据它来访问static文件夹下面的poster
        title_dct=dict(zip(title,range(len(title))))
        # print(title_dct)
        # print(path)
        for i,line in enumerate(reader):
            m=Movie.objects.create(name=line[title_dct['name']],
                                 imdb_id=line[title_dct['id']],
                                 time=line[title_dct['time']],
                                 release_time=line[title_dct['release_time']],
                                 intro=line[title_dct['intro']],
                                 director=line[title_dct['directors']],
                                 writers=line[title_dct['writers']],
                                 actors=line[title_dct['starts']])
            # 必须要先保存才能建立关系
            m.save()
            # 建立类型关系
            for genre in line[title_dct['genre']].split('|'):
                # 找到类型 genre_object
                go=Genre.objects.filter(name=genre).first()
                # print(go)
                m.genre.add(go)
            if i%1000==0:
                print(i)    # 控制台查看进度用
            # pass

def get_user_and_rating():
    '''
    获取ratings文件，设置用户信息和对电影的评分
    由于用户没有独立的信息，默认用这种方式保存用户User: name=userId,password=userId,email=userId@1.com
    通过imdb_id对电影进行关联，设置用户对电影的评分,comment默认为空
    '''
    path = os.path.join(BASE, r'rango\static\movie\info\ratings.csv')
    with open(path) as fb:
        reader=csv.reader(fb)
        # userId,movieId,rating,timestamp,timestamp不用管
        title=reader.__next__()
        title_dct=dict(zip(title,range(len(title))))
        # csv文件中，一条记录就是一个用户对一部电影的评分和时间戳，一个用户可能有多条评论
        # 所以要先取出用户所有的评分，设置成一个字典,格式为{ user:{movie1:rating, movie2:rating, ...}, ...}
        user_id_dct=dict()
        for line in reader:
            user_id=line[title_dct['userId']]
            imdb_id=line[title_dct['movieId']]
            rating=line[title_dct['rating']]
            user_id_dct.setdefault(user_id,dict())
            user_id_dct[user_id][imdb_id]=rating
    # 对所有用户和评分记录
    for user_id,ratings in user_id_dct.items():
        u=User.objects.create(name=user_id,password=user_id,email=f'{user_id}@1.com')
        # 必须先保存
        u.save()
        # 开始加入评分记录
        for imdb_id,rating in ratings.items():
            # Movie_rating(uid=)
            movie=Movie.objects.get(imdb_id=imdb_id)
            relation=Movie_rating(user=u,movie=movie,score=rating,comment='')
            relation.save()
            # break
        print(f'{user_id} process success')
        # break



if __name__ == '__main__':
    print("Starting...")
    get_genre()
    get_movie_info()
    get_user_and_rating()
    print("OK...")
