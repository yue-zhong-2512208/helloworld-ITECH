import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Movie

def populate():
    action_movies = [
        {'title': 'The Dark Knight', 'year': '2008', 'movieid': '1',
         'url': 'https://www.imdb.com/title/tt0468569/?ref_=adv_li_tt', 'movie_likes': '45', 
         'story': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'},
        
        {'title': 'The Lord of the Rings: The Return of the King', 'year': '2003', 'movieid': '2',
         'url': 'https://www.imdb.com/title/tt0167260/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.'},
        
        {'title': 'Inception', 'year': '2010', 'movieid': '3',
         'url': 'https://www.imdb.com/title/tt1375666/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'},
        
        {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'year': '2001', 'movieid': '4',
         'url': 'https://www.imdb.com/title/tt0120737/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'},

        {'title': 'Brothers in Arms', 'year': '2016', 'movieid': '5',
         'url': 'https://www.imdb.com/title/tt5813916/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'In a desolate war zone where screams of the innocent echo, seven Maroon Berets will dance with death on the very line between disaster and valor.'},
        ]

    musical_movies = [
        {'title': 'The Lion King', 'year': '1994', 'movieid': '6',
         'url': 'https://www.imdb.com/title/tt0110357/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.'},

        {'title': 'Hamilton', 'year': '2020', 'movieid': '7',
         'url': 'https://www.imdb.com/title/tt8503618/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The real life of one of America\'s foremost founding fathers and first Secretary of the Treasury, Alexander Hamilton. Captured live on Broadway from the Richard Rodgers Theater with the original Broadway cast.'},

        {'title': 'Anand', 'year': '2010', 'movieid': '8',
         'url': 'https://www.imdb.com/title/tt0066763/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The story of a terminally ill man who wishes to live life to the fullest before the inevitable occurs, as told by his best friend.'},

        {'title': 'Singin\' in the Rain', 'year': '1952', 'movieid': '9',
         'url': 'https://www.imdb.com/title/tt0045152/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'A silent film production company and cast make a difficult transition to sound.'},

        {'title': 'Sholay', 'year': '1975', 'movieid': '10',
         'url': 'https://www.imdb.com/title/tt0073707/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'After his family is murdered by a notorious and ruthless bandit, a former police officer enlists the services of two outlaws to capture the bandit.'},
    ]

    romance_movies = [
        {'title': 'Forrest Gump', 'year': '1994', 'movieid': '11',
         'url': 'https://www.imdb.com/title/tt0109830/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.'},

        {'title': 'Life Is Beautiful', 'year': '1997', 'movieid': '12',
         'url': 'https://www.imdb.com/title/tt0118799/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor, and imagination to protect his son from the dangers around their camp.'},

        {'title': 'Cinema Paradiso', 'year': '1988', 'movieid': '13',
         'url': 'https://www.imdb.com/title/tt0095765/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'A filmmaker recalls his childhood when falling in love with the pictures at the cinema of his home village and forms a deep friendship with the cinema\'s projectionist.'},

        {'title': 'Casablanca', 'year': '1942', 'movieid': '14',
         'url': 'https://www.imdb.com/title/tt0034583/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'A cynical expatriate American cafe owner struggles to decide whether or not to help his former lover and her fugitive husband escape the Nazis in French Morocco.'},

        {'title': 'Modern Times', 'year': '1936', 'movieid': '15',
         'url': 'https://www.imdb.com/title/tt0027977/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The Tramp struggles to live in modern industrial society with the help of a young homeless woman.'},
    ]
    
    sport_movies = [
        {'title': 'Dangal', 'year': '2016', 'movieid': '16',
         'url': 'https://www.imdb.com/title/tt5074352/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.'},

        {'title': 'Children of Heaven', 'year': '1997', 'movieid': '17',
         'url': 'https://www.imdb.com/title/tt0118849/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'After a boy loses his sister\'s pair of shoes, he goes on a series of adventures in order to find them. When he can\'t, he tries a new way to "win" a new pair.'},

        {'title': 'Bhaag Milkha Bhaag', 'year': '2013', 'movieid': '18',
         'url': 'https://www.imdb.com/title/tt2356180/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The truth behind the ascension of Milkha Singh who was scarred because of the India-Pakistan partition.'},

        {'title': 'Paan Singh Tomar', 'year': '2012', 'movieid': '19',
         'url': 'https://www.imdb.com/title/tt1620933/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'The story of Paan Singh Tomar, an Indian athlete and seven-time national steeplechase champion who becomes one of the most feared dacoits in Chambal Valley after his retirement.'},

        {'title': 'Chak De! India', 'year': '2007', 'movieid': '20',
         'url': 'https://www.imdb.com/title/tt0871510/?ref_=adv_li_tt', 'movie_likes': '45',
         'story': 'Kabir Khan, the coach of the Indian Women\'s National Hockey Team, dreams of making his all-girls team emerge victorious against all odds.'},
    ]
        
    cats = {
        'Action': {'movies': action_movies}, 
        'Musical': {'movies': musical_movies},
        'Romance': {'movies': romance_movies},
        'Sport': {'movies': sport_movies},
        }

    for cat, cat_data in cats.items():  
        c = add_cat(
            cat)
        for p in cat_data['movies']:
            add_movie(c, p['title'], p['year'], p['movieid'], p['url'], p['movie_likes'], p['story'])

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_movie(cat, title, year, movieid, url, movie_likes, story): 
    p = Movie.objects.get_or_create(category=cat, title=title)[0] 
    p.year = year
    p.movieid = movieid
    p.url = url 
    p.movie_likes = movie_likes
    p.story = story
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0] 
    c.save() 
    return c

# Start execution here!
if __name__ == '__main__': 
    print('Starting Rango population script...') 
    populate()
