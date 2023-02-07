import json
filename = 'books_united_schema_mongo_id.json'


books_model = {}
books_model_list = list(books_model['fields'].keys())
print(books_model_list)


with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))

    for index, item in enumerate(data):
        fields_list = list(item['fields'].keys())
        for key in books_model_list:
            if key in fields_list:
                pass
            else:
                print(key)

    print('end all')

# with open(results) as json_file:
#     data = json.load(json_file)
