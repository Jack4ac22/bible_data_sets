import json
import time
# from googletrans import Translator
# translator = Translator()
filename = './chapters/chapters.json'
results = 'chapters_united_schema_mongo_id.json'
books_model = {
    "id": "",
    "fields":
    {
        "osisRef": "",
        "book": [],
        "bookPropreName": [],
        "chapterNum": "",
        "writer": [],
        "verses": "",
        "verses_os": "",
        "slug": "",
        "peopleCount": "",
        "peoples": [],
        "placesCount": "",
        "places": [],
        "writer count": ""
    }
}
books_model_list = list(books_model['fields'].keys())
print(books_model_list)


with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))
    new_list = []

    for index, item in enumerate(data):
        fields_list = list(item['fields'].keys())
        new_item = {}
        new_item['_id'] = item['id']
        new_item['status'] = None
        new_item['fields'] = {}
        for key in books_model_list:
            if key in fields_list:
                new_item['fields'][key] = item['fields'][key]
            elif key == "bookPropreName":
                pass
            elif key == "testament_ar":
                pass
            elif key == "peoples":
                pass
            elif key == "verses_os":
                # osis_verses
                verses = item["fields"]['verses']
                print(verses)
                osisRefV = []
                with open('./verses/verses.json') as verses_json_file:
                    verses_id_changing = json.load(verses_json_file)
                    for verse_str_id in verses:
                        for ver_os in verses_id_changing:
                            if ver_os['id'] == verse_str_id:
                                osisRefV.append(ver_os['fields']['osisRef'])
                new_item['fields']['verses_os'] = osisRefV
            else:
                new_item['fields'][key] = ""

        new_list.append(new_item)
        print(len(new_list))

        f = open(results, "w")
        f.write((json.dumps(new_list)))
        f.close()
        print('end', index)
    print('end all')

# with open(results) as json_file:
#     data = json.load(json_file)
