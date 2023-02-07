import json
filename = './chapters/chapters.json'
results = 'chapters_keys.json'
with open(filename) as json_file:
    data = json.load(json_file)
    new_dictionary = {}
    for item in data:
        chapters_field_keys_list = list(item['fields'].keys())
        for field_key in chapters_field_keys_list:
            if field_key not in new_dictionary:
                new_dictionary[field_key]=""
    f = open(results, "w")
    f.write((json.dumps(new_dictionary)))
    f.close()