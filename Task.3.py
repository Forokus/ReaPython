import Json

if __name__ == '__main__':
	keyword = input('Введите ключевое слово: ')
	spisok = Json.decode_json('res')
	
	all_title = []
	for title in spisok.keys():
		if keyword.lower() in title.lower().split():
			all_title.append(title)
			
	print('\nРезульт:\n')
	for title in all_title:
		print(title)