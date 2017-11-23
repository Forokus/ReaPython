import Json
import tmdb

try:
	keyword = input('Введите название фильма: ')
	recommendation = tmdb.recommend(keyword)
	print('\nРекомендуемые фильмы:\n')
	for film in recommendation.keys():
		print(film)
except UnicodeEncodeError:
    pass