import json
import time
from translate_function import translate_this, updateText
filename = 'people.json'
results = 'people_united_schema_1.json'

people_model = {
    "id": "",
    "fields": {
        "personLookup": "",
        "personID": 2657,
        "name": "",
        "surname": "",
        "alsoCalled": "",
        "isProperName": True,
        "gender": "Male",
        "memberOf": ["peiple_group_id"],
        "birthPlace": ["places_id"],
        "verses": ["verse_id"],
        "siblings": ["people_id"],
        "halfSiblingsSameFather": ["people_id"],
        "halfSiblingsSameMother": ["people_id"],
        "mother": ["people_id"],
        "father": ["people_id"],
        "children": ["people_id"],
        "partners": ["people_id"],
        "displayTitle": "Shephatiah",
        "status": "wip",
        "ambiguous": True,
        "Disambiguation (temp)": "....",
        "verseCount": 2,
        "minYear": -1053,
        "maxYear": -1048,
        "birthYear": -1048,
        "deathYear": -1048,
        "alphaGroup": "S",
        "alphaGroup_ar": "S",
        "slug": "shephatiah_2657",
        "Easton's Count": 0,
        "eastons": ["eston_id"],
        "events": ["event_id"],
        "deathPlace": ["places_id"],
        "chaptersWritten": ["chapter_id"],
        "timeline": ["event_id"],
        "eventGroups": ["", ""],
        "dictText": [""],
        "dictionaryLink": [""],
        "dictionaryText": [""]
    },
    "createdTime": "2018-03-19T00:26:39.000Z"
}
people_model_list = list(people_model['fields'].keys())
print(people_model_list)


with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))
    new_list = []

    for index, item in enumerate(data):
        fields_list = list(item['fields'].keys())
        new_item = {}
        new_item['id'] = item['id']
        new_item['status'] = None
        new_item['fields'] = {}
        for key in people_model_list:
            if key in fields_list:
                new_item['fields'][key] = item['fields'][key]
                if key in ["name", "surname", "alsoCalled", "Disambiguation", "displayTitle", "dictionaryText"]:
                    try:
                        text = item['fields'][key]
                        translated_key = updateText(text,900)
                        new_item['fields'][key+'_ar'] = translated_key
                    except:
                        new_item['fields'][key+'_ar'] = ''
                        print("translation error", item['fields'][key])
                if key in ["eventGroups", "dictText"]:
                    translated_item = []
                    for text_by_index in item['fields'][key]:
                        try:
                            translated_key = updateText(text_by_index,900)
                            translated_item.append(translated_key)
                        except:
                            pass
                    new_item['fields'][key+'_ar'] = translated_item    
            else:
                new_item['fields'][key] = None

        new_list.append(new_item)
        print(len(new_list))

        f = open(results, "w")
        f.write((json.dumps(new_list)))
        f.close()
        print('end', index)
        if index % 10 == 0:
            print(index % 10)
            print('sleeping')
            # time.sleep(60)
            print('waking up')

    print('end all')

# with open(results) as json_file:
#     data = json.load(json_file)
