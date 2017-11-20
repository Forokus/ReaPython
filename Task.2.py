import urllib.request
import urllib.parse
import json


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
	


spisok = []
n = 1
ckachali = 0
while ckachali <= 1000:
	try:
		result = get_movie_details(n, "228d3d959f0b90051acf789518d19c0d")
		spisok.append(result)
		ckachali+=1
	except:
		None
	n+=1

for e in spisok:
	print(json.dumps(e).encode('utf-8'))