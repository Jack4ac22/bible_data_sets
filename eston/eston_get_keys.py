import json
filename = './eston/easton.json'
results = 'eston_keys.json'
with open(filename) as json_file:
    data = json.load(json_file)
    new_dictionary = {}
    for item in data:
        dict_field_keys_list = list(item['fields'].keys())
        for field_key in dict_field_keys_list:
            if field_key not in new_dictionary:
                new_dictionary[field_key]=""
    f = open(results, "w")
    f.write((json.dumps(new_dictionary)))
    f.close()