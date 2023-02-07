import json
filename = 'events.json'
results = 'events_updated.json'

with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))
    new_list = []
    for index, item in enumerate(data):
        title = data[index]['fields']['title']
        from googletrans import Translator
        translator = Translator()
        res = translator.translate(title, dest='ar')
        print(index)
        data[index]['fields']['ar_title'] = res.__dict__()["text"]
        new_list.append(data[index])
    f = open(results, "w")
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
