import json
filename = 'books.json'
results = 'book_updated_writers_osis.json'
translations = {"Pentateuch": "الشريعة", "Historical": "الأسفار التاريخية",
                "Poetry-Wisdom": "الأسفار الشعرية/الحكمة", "Major Prophets": "الأنبياء الكبار", "Minor Prophets": "الأنبياء الصغار", "Gospels": "البشائر/الأناجيل", "Acts": "أعمال الرسل", "Pauline Epistles": "الرسائل البولسية", "General Epistles": "الرسائل الجامعة", "Revelation": "سفر الرؤيا"}
translations1 = {"New Testament": "العهد الجديد",
                 "Old Testament": "العهد القديم"}
with open('../people/people.json') as people_json_file:
    people = json.load(people_json_file)
with open(filename) as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(len(data))
    new_list = []
    for index, item in enumerate(data):
        title = data[index]['fields']['bookDiv']
        item['fields']['ar_title'] = translations[title]
        print(item['fields']["ar_title"])
        testament = data[index]['fields']['testament']
        item['fields']['ar_testament'] = translations1[testament]
        # osis_verses
        verses = item["fields"]['verses']
        osisRefV = []
        with open('../verses/verses.json') as verses_json_file:
            verses_id_changing = json.load(verses_json_file)
            for verse_str_id in verses:
                for ver_os in verses_id_changing:
                    if ver_os['id'] == verse_str_id:
                        osisRefV.append(ver_os['fields']['osisRef'])
        item['fields']['verses_os'] = osisRefV

        # osis_chapters
        chapters = item['fields']['chapters']
        oisisRefChapters = []
        with open('chapters.json') as verses_json_file:
            chapters_id_changing = json.load(verses_json_file)
            for chapter_str_id in chapters:
                for chapter_os in chapters_id_changing:
                    if chapter_os['id'] == verse_str_id:
                        oisisRefChapters.append(
                            chapter_os['fields']['osisRef'])
        item['fields']['chapters_os'] = oisisRefChapters

        # fixing the writers from a string to search to the id of the person in people.json
        writers = item["fields"]["writers"]
        item["fields"]["writers_id"] = []
        new_writers = []
        for writer in writers:
            for person in people:
                if writer == person["fields"]["personLookup"]:
                    writer_new_id = person["id"]
                    new_writers.append(writer_new_id)
        item["fields"]["writers_id"] = new_writers

        new_list.append(item)
    f = open(results, "w")
    f.write((json.dumps(new_list)))
    f.close()
    print('done')
with open(results) as json_file:
    data = json.load(json_file)


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
