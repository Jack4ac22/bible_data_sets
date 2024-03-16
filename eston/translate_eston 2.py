import json
import time
from easton_translate_function import translate_this, updateText
filename = 'easton_sh.json'
results = 'eston_united_schema_sh.json'

eston_model = {
    "id": "",
    "fields": {
        "dictLookup": "Abdeel",
        "termID": "a-p18.3",
        "termLabel": "Abdeel",
        "def_id": "a-p18.4",
        "has_list": "",
        "itemNum": "",
        "matchType": "person",
        "matchSlugs": "abdeel_5",
        "dictText": "Servant of God, ([Jer. 36:26](/jer#Jer.36.26)), the father of Shelemiah.",
        "index": 11,
        "personLookup": ["recIaoifslP7mxktH"],
        "placeLookup": ["recIaoifslP7mxktH"]}
}
eston_model_list = list(eston_model['fields'].keys())
print(eston_model_list)


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
        for key in eston_model_list:
            if key in fields_list:
                new_item['fields'][key] = item['fields'][key]
                if key in ["dictLookup", "dictText"]:
                    try:
                        text = item['fields'][key]
                        translated_key = updateText(text, 2000)
                        new_item['fields'][key+'_ar'] = translated_key
                    except:
                        new_item['fields'][key+'_ar'] = ''
                        print("translation error", item['fields'][key])
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
            # print('sleeping')
            # time.sleep(60)
            # print('waking up')

    print('end all')

# with open(results) as json_file:
#     data = json.load(json_file)
