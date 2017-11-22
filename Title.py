import Json

films = Json.decode_json('res')
try:
    for title in films.keys(): 
        print(title)
except UnicodeEncodeError:
    pass