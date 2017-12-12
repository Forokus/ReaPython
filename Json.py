import json

def encode_json(name, dictionary):
	with open('{}.json'.format(name),'w') as file:
		json.dump(dictionary, file)

def decode_json(name):
	with open('{}.json'.format(name)) as file:
		encoded_coll = json.load(file)
	return encoded_coll
