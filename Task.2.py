import json
import tmdb
import Json
from os import environ


my_api_key = environ['tmdbKey']

spisok = {}
n = 1
ckachali = 0

while ckachali < 1000:
	try:
		result = tmdb.get_movie_details(n, my_api_key)
		spisok[result['title']] = result
		ckachali+=1
	except:
		None
	n+=1

Json.encode_json('res', spisok)