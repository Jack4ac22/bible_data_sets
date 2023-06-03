import json
filename = './q&a/questions.json'
with open(filename) as json_file:
    data = json.load(json_file)
    category1 = "Fill in the blank"
    category2 = "Sentence completion"
    category3 = "Multiple choice"
    category4 = "True or false"
    # category5= "Sentence completion"
    # print(len(filter()))

    print(category1, len(
        [obj for obj in data if obj['category'] == category1]))
    print(category2, len(
        [obj for obj in data if obj['category'] == category2]))
    print(category3, len(
        [obj for obj in data if obj['category'] == category3]))
    print(category4, len(
        [obj for obj in data if obj['category'] == category4]))

    # print(len(data))
filename = './systematic_theology/sys_theology_no_id.json'
with open(filename) as json_file:
    data = json.load(json_file)

    print("systematic: ", len(data))

    # print(len(data))
