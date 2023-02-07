import json
filename = 'books.json'
results = 'books_shortName.json'
with open(filename) as json_file:
    data = json.load(json_file)
    new_dictionary = {}
    for item in data:
        book_name = item['fields']['shortName']
        new_dictionary[book_name] = ''
    f = open(results, "w")
    f.write((json.dumps(new_dictionary)))
    f.close()
