import json
filename = 'people_updated_1.json'
results = 'people_updated.json'
with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))
    new_list = []
    for index, item in enumerate(data):
        print('start', index)
        print(item['fields']['personLookup'])
        # new_list.append(item)
        # name = item['fields']['name']
        # if '_' in name:
        #     name_list = name.splite('_')
        #     name = name_list[0]
        # from googletrans import Translator
        # translator = Translator()
        # translated_name = translator.translate(name, dest='ar').__dict__()["text"]
        # print(translated_name)
        item['fields']['name_ar'] = ""
        new_list.append(item)
        f = open(results, "w")
        f.write((json.dumps(new_list)))
        f.close()
        print('end', index)

with open(results) as json_file:
    data = json.load(json_file)
