import tmdb
from os import environ

my_api_key = environ['tmdbKey']
print('Введите номер фильма:')
n = int(input())
print('Бюджет фильма составляет:' + str(tmdb.get_movie_details(n, my_api_key)['budget']))