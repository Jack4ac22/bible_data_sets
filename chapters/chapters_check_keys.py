import json
filename = './chapters/chapters.json'


chapters_model = {"_id": "",
                  "status": None,
                  "fields": {
                      "osisRef": "",
                      "book": "",
                      "chapterNum": "",
                      "writer": "",
                      "verses": "",
                      "slug": "",
                      "peopleCount": "",
                      "placesCount": "",
                      "modified": "",
                      "writer count": ""
                  }}
chapters_model_list = list(chapters_model['fields'].keys())
print(chapters_model_list)


with open(filename) as json_file:
    data = json.load(json_file)
    print(type(data))
    print(len(data))

    for index, item in enumerate(data):
        fields_list = list(item['fields'].keys())
        for key in fields_list:
            if key in chapters_model_list:
                pass
            else:
                print(key)

    print('end all')

# with open(results) as json_file:
#     data = json.load(json_file)
