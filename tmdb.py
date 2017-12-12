import urllib.request
import urllib.parse
import json
import Json

def load_json_data_from_url(base_url, url_params):
	url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
	response = urllib.request.urlopen(url).read().decode('utf-8')
	return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
	extra_params = extra_params or {}
	url = 'https://api.themoviedb.org/3%s' % method
	params = {
		'api_key': api_key,
		'language': 'ru',
	}
	params.update(extra_params)
	return load_json_data_from_url(url, params)
	
def get_movie_details(n,api_key):
	return make_tmdb_api_request("/movie/"+ str(n),api_key)
	
def recommend(nazvanie_filma):
	spisok = Json.decode_json('res')
	recommendation = {}
	
	film_genre = []
	if nazvanie_filma in spisok.keys():
		for gnr in spisok[nazvanie_filma]['genres']:
			film_genre.append(gnr['name'])
	else:
		return {}

	for film in spisok.keys():
		if film == nazvanie_filma:
			next
		for genre in spisok[film]['genres']:
			if genre['name'] in film_genre:
				recommendation[film] = spisok[film]
				break
	return recommendation
