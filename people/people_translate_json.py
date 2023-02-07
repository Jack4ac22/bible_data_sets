import json
filename = 'people.json'
results = 'people_updated.json'

with open(filename) as json_file:
    data = json.load(json_file)
    # print(data[0]['fields'].keys())
    # print(type(data))
    print(len(data))  # 3069
    new_list = []
    # for index, item in enumerate(data):
    for index, item in enumerate(data):
        name = data[index]['fields']['name']
        if 'dictText' in data[index]['fields']:
            dict_text = data[index]['fields']['dictText']
            # print(dict_text)
        from googletrans import Translator
        translator = Translator()
        try:
            res_name = translator.translate(name, dest='ar')
        except:
            print("not", index)
        # TODO: translating the Arabic text is too long:
        # if dict_text:
        #     print("dict is there")
        #     print(type(dict_text))
        #     ar_dic_text = []
        #     for i in dict_text:
        #         print(type(i))
        #         print(i)
        #         try:
        #             res_dict_text = translator.translate(i, dest='ar')
        #             print(res_dict_text.__dict__()['text'])
        #             ar_dic_text.append(res_dict_text.__dict__()["text"])
        #             print(ar_dic_text)
        #         except:
        #             pass
        # if dict_text:
        #     data[index]['fields']['ar_dictText'] = ar_dic_text
        print(index)
        # print(res_name.__dict__()['text'])
        data[index]['fields']['ar_name'] = res_name.__dict__()["text"]
        verses = item["fields"]['verses']
        osisRefV = []
        with open('../verses/verses.json') as verses_json_file:
            verses_id_changing = json.load(verses_json_file)
            for verse_str_id in verses:
                for ver_os in verses_id_changing:
                    if ver_os['id'] == verse_str_id:
                        osisRefV.append(ver_os['fields']['osisRef'])
        item['fields']['verses_os'] = osisRefV
        new_list.append(data[index])
    f = open(results, "a")
    f.write((json.dumps(new_list)))
    f.close()
    print('done')


# updated_file = {}
# for row in data:
#         reference = data[row]['v']
#         items = reference.split(' ')
#         id = row
#         book = items[0].lower().title()
#         chapter = items[1]
#         verse_n = items[2]
#         if "r" in data[row]:
#             cross_references = data[row]['r']
#             the_list = []
#             for referenc_cross in cross_references:
#                 references = cross_references[referenc_cross]
#                 verse = cross_references[referenc_cross].split(' ')
#                 cros_id = referenc_cross
#                 cros_book = verse[0].lower().title()
#                 cros_chapter = verse[1]
#                 cros_verse = verse[2]
#                 verse_to_append = {'id': cros_id, 'book_id': cros_book,
#                                    'chapter_number': cros_chapter, 'verse_number': cros_verse, 'verse_id': cros_book+'.'+cros_chapter+'.'+cros_verse}
#                 the_list.append(verse_to_append)
#             original_verse = {'id': id, 'book_id': book, 'chapter_number': chapter,
#                               'verse_number': verse_n, 'verse_id': book+'.'+chapter+'.'+verse_n, 'cross_references': the_list}
#             # print(the_list)
#             updated_file[row] = original_verse

#             # print(updated_file)
#     f = open(results, "w")
#     f.write((json.dumps(updated_file)))
#     f.close()
