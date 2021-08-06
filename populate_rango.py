import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Movie

def populate():
    action_movies = [
        {'title': 'The Dark Knight', 'year': '2008', 'posternum': '1',
         'url': 'https://www.imdb.com/title/tt0468569/?ref_=adv_li_tt', 'likes': '45', 'views': '253', 
         'story': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'},
        
        {'title': 'The Lord of the Rings: The Return of the King', 'year': '2003', 'posternum': '2',
         'url': 'https://www.imdb.com/title/tt0167260/?ref_=adv_li_tt', 'likes': '74', 'views': '366',
         'story': 'Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.'},
        
        {'title': 'Inception', 'year': '2010', 'posternum': '3',
         'url': 'https://www.imdb.com/title/tt1375666/?ref_=adv_li_tt', 'likes': '35', 'views': '767',
         'story': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'},
        
        {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'year': '2001', 'posternum': '4',
         'url': 'https://www.imdb.com/title/tt0120737/?ref_=adv_li_tt', 'likes': '34', 'views': '678',
         'story': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'},

        {'title': 'Brothers in Arms', 'year': '2016', 'posternum': '5',
         'url': 'https://www.imdb.com/title/tt5813916/?ref_=adv_li_tt', 'likes': '65', 'views': '467', 
         'story': 'In a desolate war zone where screams of the innocent echo, seven Maroon Berets will dance with death on the very line between disaster and valor.'},
        ]

    musical_movies = [
        {'title': 'The Lion King', 'year': '1994', 'posternum': '6',
         'url': 'https://www.imdb.com/title/tt0110357/?ref_=adv_li_tt', 'likes': '23', 'views': '126',
         'story': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.'},

        {'title': 'Hamilton', 'year': '2020', 'posternum': '7',
         'url': 'https://www.imdb.com/title/tt8503618/?ref_=adv_li_tt', 'likes': '75', 'views': '245', 
         'story': 'The real life of one of America\'s foremost founding fathers and first Secretary of the Treasury, Alexander Hamilton. Captured live on Broadway from the Richard Rodgers Theater with the original Broadway cast.'},

        {'title': 'Anand', 'year': '2010', 'posternum': '8',
         'url': 'https://www.imdb.com/title/tt0066763/?ref_=adv_li_tt', 'likes': '64', 'views': '253',
         'story': 'The story of a terminally ill man who wishes to live life to the fullest before the inevitable occurs, as told by his best friend.'},

        {'title': 'Singin\' in the Rain', 'year': '1952', 'posternum': '9',
         'url': 'https://www.imdb.com/title/tt0045152/?ref_=adv_li_tt', 'likes': '38', 'views': '658',
         'story': 'A silent film production company and cast make a difficult transition to sound.'},

        {'title': 'Sholay', 'year': '1975', 'posternum': '10',
         'url': 'https://www.imdb.com/title/tt0073707/?ref_=adv_li_tt', 'likes': '35', 'views': '456',
         'story': 'After his family is murdered by a notorious and ruthless bandit, a former police officer enlists the services of two outlaws to capture the bandit.'},
    ]

    romance_movies = [
        {'title': 'Forrest Gump', 'year': '1994', 'posternum': '11',
         'url': 'https://www.imdb.com/title/tt0109830/?ref_=adv_li_tt', 'likes': '84', 'views': '366',
         'story': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.'},

        {'title': 'Life Is Beautiful', 'year': '1997', 'posternum': '12',
         'url': 'https://www.imdb.com/title/tt0118799/?ref_=adv_li_tt', 'likes': '84', 'views': '364', 
         'story': 'When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor, and imagination to protect his son from the dangers around their camp.'},

        {'title': 'Cinema Paradiso', 'year': '1988', 'posternum': '13',
         'url': 'https://www.imdb.com/title/tt0095765/?ref_=adv_li_tt', 'likes': '34', 'views': '667',
         'story': 'A filmmaker recalls his childhood when falling in love with the pictures at the cinema of his home village and forms a deep friendship with the cinema\'s projectionist.'},

        {'title': 'Casablanca', 'year': '1942', 'posternum': '14',
         'url': 'https://www.imdb.com/title/tt0034583/?ref_=adv_li_tt', 'likes': '36', 'views': '376',
         'story': 'A cynical expatriate American cafe owner struggles to decide whether or not to help his former lover and her fugitive husband escape the Nazis in French Morocco.'},

        {'title': 'Modern Times', 'year': '1936', 'posternum': '15',
         'url': 'https://www.imdb.com/title/tt0027977/?ref_=adv_li_tt', 'likes': '95', 'views': '458',
         'story': 'The Tramp struggles to live in modern industrial society with the help of a young homeless woman.'},
    ]
    
    sport_movies = [
        {'title': 'Dangal', 'year': '2016', 'posternum': '16',
         'url': 'https://www.imdb.com/title/tt5074352/?ref_=adv_li_tt', 'likes': '34', 'views': '843',
         'story': 'Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.'},

        {'title': 'Children of Heaven', 'year': '1997', 'posternum': '17',
         'url': 'https://www.imdb.com/title/tt0118849/?ref_=adv_li_tt', 'likes': '53', 'views': '496', 
         'story': 'After a boy loses his sister\'s pair of shoes, he goes on a series of adventures in order to find them. When he can\'t, he tries a new way to "win" a new pair.'},

        {'title': 'Bhaag Milkha Bhaag', 'year': '2013', 'posternum': '18',
         'url': 'https://www.imdb.com/title/tt2356180/?ref_=adv_li_tt', 'likes': '25', 'views': '569',
         'story': 'The truth behind the ascension of Milkha Singh who was scarred because of the India-Pakistan partition.'},

        {'title': 'Paan Singh Tomar', 'year': '2012', 'posternum': '19',
         'url': 'https://www.imdb.com/title/tt1620933/?ref_=adv_li_tt', 'likes': '62', 'views': '758',
         'story': 'The story of Paan Singh Tomar, an Indian athlete and seven-time national steeplechase champion who becomes one of the most feared dacoits in Chambal Valley after his retirement.'},

        {'title': 'Chak De! India', 'year': '2007', 'posternum': '20',
         'url': 'https://www.imdb.com/title/tt0871510/?ref_=adv_li_tt', 'likes': '75', 'views': '564',
         'story': 'Kabir Khan, the coach of the Indian Women\'s National Hockey Team, dreams of making his all-girls team emerge victorious against all odds.'},
    ]

    biography_movies = [
        {'title': 'Schindler\'s List', 'year': '1993', 'posternum': '21',
         'url': 'https://www.imdb.com/title/tt0108052/?ref_=adv_li_tt', 'likes': '85', 'views': '765',
         'story': 'In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.'},

        {'title': 'Goodfellas', 'year': '1990', 'posternum': '22',
         'url': 'https://www.imdb.com/title/tt0099685/?ref_=adv_li_tt', 'likes': '86', 'views': '867',
         'story': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.'},

        {'title': 'Untouchable', 'year': '2011', 'posternum': '23',
         'url': 'https://www.imdb.com/title/tt1675434/?ref_=adv_li_tt', 'likes': '73', 'views': '945',
         'story': 'After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.'},

        {'title': 'The Pianist', 'year': '2002', 'posternum': '24',
         'url': 'https://www.imdb.com/title/tt0253474/?ref_=adv_li_tt', 'likes': '76', 'views': '657',
         'story': 'A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto of World War II.'},

        {'title': 'Braveheart', 'year': '1995', 'posternum': '25',
         'url': 'https://www.imdb.com/title/tt0112573/?ref_=adv_li_tt', 'likes': '56', 'views': '846',
         'story': 'Scottish warrior William Wallace leads his countrymen in a rebellion to free his homeland from the tyranny of King Edward I of England.'},
    ]

    mystery_movies = [
        {'title': 'Spirited Away', 'year': '2001', 'posternum': '26',
         'url': 'https://www.imdb.com/title/tt0245429/?ref_=adv_li_tt', 'likes': '97', 'views': '574',
         'story': 'During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.'},

        {'title': 'The Green Mile', 'year': '1999', 'posternum': '27',
         'url': 'https://www.imdb.com/title/tt0120689/?ref_=adv_li_tt', 'likes': '65', 'views': '856',
         'story': 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.'},

        {'title': 'Seven', 'year': '1995', 'posternum': '28',
         'url': 'https://www.imdb.com/title/tt0114369/?ref_=adv_li_tt', 'likes': '56', 'views': '567',
         'story': 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.'},

        {'title': 'Harakiri', 'year': '1962', 'posternum': '29',
         'url': 'https://www.imdb.com/title/tt0056058/?ref_=adv_li_tt', 'likes': '86', 'views': '357',
         'story': 'When a ronin requesting seppuku at a feudal lord\'s palace is told of the brutal suicide of another ronin who previously visited, he reveals how their pasts are intertwined - and in doing so challenges the clan\'s integrity.'},

        {'title': 'Raatchasan', 'year': '2018', 'posternum': '30',
         'url': 'https://www.imdb.com/title/tt7060344/?ref_=adv_li_tt', 'likes': '45', 'views': '546',
         'story': 'A sub-inspector sets out in pursuit of a mysterious serial killer who targets teen school girls and murders them brutally.'},
    ]
        
    cats = {
        'Action': {'movies': action_movies}, 
        'Musical': {'movies': musical_movies},
        'Romance': {'movies': romance_movies},
        'Sport': {'movies': sport_movies},
        'Biography': {'movies': biography_movies},
        'Mystery': {'movies': mystery_movies},
        }

    for cat, cat_data in cats.items():  
        c = add_cat(
            cat)
        for p in cat_data['movies']:
            add_movie(c, p['title'], p['year'], p['posternum'], p['url'],
                      p['likes'], p['views'], p['story'])

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_movie(cat, title, year, posternum, url, likes, views, story): 
    p = Movie.objects.get_or_create(category=cat, title=title)[0] 
    p.year = year
    p.posternum = posternum
    p.url = url 
    p.likes = likes
    p.views = views
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
