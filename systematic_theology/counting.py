import json
filename = 'systematic_theology/sys_theology_no_id.json'
with open(filename) as json_file:
    data = json.load(json_file)
    print(len(data))