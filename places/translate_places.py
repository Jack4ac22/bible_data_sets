import json
import time
from translate_function import translate_this, updateText
filename = 'places/places.json'
results = 'places/places_united_schema.json'
peopleFile = 'people/people_united_schema.json'
people_model = {
    "id": "",
    "fields": {
        "placeLookup": "",
        "openBibleLat": "",
        "openBibleLong": "",
        "kjvName": "",
        "esvName": "",
        "comment": "",
        "featureType": "",
        "placeID": "",
        "recogitoUri": "",
        "recogitoLat": "",
        "recogitoLon": "",
        "verses": "",
        "recogitoStatus": "",
        "recogitoLabel": "",
        "recogitoUID": "",
        "status": "",
        "displayTitle": "",
        "eastons": "",
        "featureSubType": "",
        "verseCount": "",
        "latitude": "",
        "longitude": "",
        "alphaGroup": "",
        "slug": "",
        "dictText": "",
        "rootID": "",
        "peopleDied": "",
        "precision": "",
        "recogitoType": "",
        "hasBeenHere": "",
        "timeline": "",
        "dictionaryLink": "",
        "dictionaryText": "",
        "recogitoComments": "",
        "eventsHere": "",
        "eventGroups": "",
        "ambiguous": "",
        "aliases": "",
        "booksWritten": "",
        "duplicate_of": "",
        "peopleBorn": ""
    }
}
people_model_list = list(people_model['fields'].keys())
print(people_model_list)

with open(peopleFile) as peopl_file:
    people_data = json.load(peopl_file)

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
                    if key in ["kjvName", "dictionaryText", "displayTitle"]:
                        try:
                            text = item['fields'][key]
                            translated_key = updateText(text, 900)
                            new_item['fields'][key+'_ar'] = translated_key
                        except:
                            new_item['fields'][key+'_ar'] = ''
                            print("translation error", item['fields'][key])
                    if key in ["dictText"]:
                        translated_item = []
                        for text_by_index in item['fields'][key]:
                            try:
                                translated_key = updateText(text_by_index, 900)
                                translated_item.append(translated_key)
                            except:
                                pass
                        new_item['fields'][key+'_ar'] = translated_item
                    if key in ["hasBeenHere"]:
                        new_list_has_been_here = []
                        people_as_list = (item['fields'][key]).split(", ")
                        if len(people_as_list) > 0:
                            for person_lookup in people_as_list:
                                for person_from_file in people_data:
                                    if person_lookup == person_from_file['fields']['personLookup']:
                                        person_id = person_from_file['id']
                                        new_list_has_been_here.append(person_id)
                        new_item['fields'][key+'_ar'] = new_list_has_been_here
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
