import json
import time
# from googletrans import Translator
# translator = Translator()
filename = 'books.json'
results = 'books_united_schema_mongo_id.json'
arabic_books = {
    "Genesis": "سفر التكوين",
    "Exodus": "سفر الخروج",
    "Leviticus": "سفر اللاويّين",
    "Numbers": "سفر العدد",
    "Deuteronomy": "سفر التثنية",
    "Joshua": "سفر يشوع",
    "Judges": "سفر القُضاة",
    "Ruth": "سفر راعوث",
    "1 Samuel": "صموئيل سفر الأول",
    "2 Samuel": "صموئيل سفر الثاني",
    "1 Kings": "الملوك سفر الأول",
    "2 Kings": "الملوك سفر الثاني",
    "1 Chronicles": "أخبار الأيام سفر الأول",
    "2 Chronicles": "أخبار الأيام سفر الثاني",
    "Ezra": "سفر عزرا",
    "Nehemiah": "سفر نحميا",
    "Esther": "سفر استير",
    "Job": "سفر أيوب",
    "Psalms": "سفر المزامير",
    "Proverbs": "سفر الأمثال",
    "Ecclesiastes": "سفر الجامعة",
    "Song of Solomon": "نشيد سفر الأنشاد",
    "Isaiah": "سفر اشعياء",
    "Jeremiah": "سفر ارمياء",
    "Lamentations": "سفر المراثي",
    "Ezekiel": "سفر حزقيال",
    "Daniel": "سفر دانيال",
    "Hosea": "سفر هوشع",
    "Joel": "سفر يوئيل",
    "Amos": "سفر آموص",
    "Obadiah": "سفر عوبيديا",
    "Jonah": "سفر يونان",
    "Micah": "سفر ميخا",
    "Nahum": "سفر ناحوم",
    "Habakkuk": "سفر حبقوق",
    "Zephaniah": "سفر صفنيا",
    "Haggai": "سفر حجَّاي",
    "Zechariah": "سفر زكريا",
    "Malachi": "سفر ملاخي",
    "Matthew": "الإنجيل كما دوَّنه متى",
    "Mark": "الإنجيل كما دوَّنه مرقس",
    "Luke": "الإنجيل كما دوَّنه لوقا",
    "John": "الإنجيل كما دوَّنه يوحنا",
    "Acts": "سفر أعمال الرسل",
    "Romans": "الرسالة إلى أهل رومية",
    "1 Corinthians": "الرسالة الأولى إلى أهل كورنثوس",
    "2 Corinthians": "الرسالة الثانية إلى أهل كورنثوس",
    "Galatians": "الرسالة إلى أهل غلاطية",
    "Ephesians": "الرسالة إلى أهل أفسس",
    "Philippians": "الرسالة إلى أهل فيليبي",
    "Colossians": "الرسالة إلى أهل كولوسي",
    "1 Thessalonians": "الرسالة الأولى إلى أهل تسالونيكي",
    "2 Thessalonians": "الرسالة الثانية إلى أهل تسالونيكي",
    "1 Timothy": "رسالة تيموثاوس الأولى",
    "2 Timothy": "رسالة تيموثاوس الثانية",
    "Titus": "الرسالة إلى تيطس",
    "Philemon": "الرسالة إلى فيليمون",
    "Hebrews": "الرسالى إلى العبرانيين",
    "James": "رسالى يعقوب الجامعة",
    "1 Peter": "رسالى بطرس الأولى",
    "2 Peter": "رسالى بطرس الثانية",
    "1 John": "رسالة يوحنا الأولى",
    "2 John": "رسالة يوحنا الثانية",
    "3 John": "رسالة يوحنا الثالثة",
    "Jude": "رسالة يهوذا",
    "Revelation": "سفر الرؤيا"
}
arabic_divisions = {"Pentateuch": "الشريعة", "Historical": "الأسفار التاريخية",
                    "Poetry-Wisdom": "الأسفار الشعرية/الحكمة", "Major Prophets": "الأنبياء الكبار", "Minor Prophets": "الأنبياء الصغار", "Gospels": "البشائر/الأناجيل", "Acts": "أعمال الرسل", "Pauline Epistles": "الرسائل البولسية", "General Epistles": "الرسائل الجامعة", "Revelation": "سفر الرؤيا"}
arabic_testaments = {"New Testament": "العهد الجديد",
                     "Old Testament": "العهد القديم"}
arabic_shortName = {
    "Ge": "تك",
    "Ex": "خر",
    "Le": "لا",
    "Nu": "عد",
    "Dt": "تث",
    "Jos": "يش",
    "Jdg": "قض",
    "Ru": "را",
    "1Sa": "١ صم",
    "2Sa": "٢ صم",
    "1Ki": "١ مل",
    "2Ki": "٢ مل",
    "1Ch": "١ أخ",
    "2Ch": "٢ أخ",
    "Ezr": "عز",
    "Ne": "نح",
    "Es": "أس",
    "Job": "أي",
    "Ps": "مز",
    "Pr": "أم",
    "Ec": "جا",
    "So": "نش",
    "Is": "إش",
    "Je": "إر",
    "La": "مرا",
    "Eze": "حز",
    "Da": "دا",
    "Ho": "هو",
    "Joe": "يؤ",
    "Am": "عا",
    "Ob": "عو",
    "Jon": "يون",
    "Mic": "مي",
    "Na": "نا",
    "Hab": "حب",
    "Zep": "صف",
    "Hag": "حج",
    "Zec": "زك",
    "Mal": "ملا",
    "Mt": "مت",
    "Mk": "مر",
    "Lu": "لو",
    "Jn": "يو",
    "Ac": "أع",
    "Ro": "رو",
    "1Co": "١ كو",
    "2Co": "٢ كو",
    "Ga": "غلا",
    "Eph": "أف",
    "Php": "في",
    "Col": "كو",
    "1Th": "١ تس",
    "2Th": "٢ تس",
    "1Ti": "١ تي",
    "2Ti": "٢ تي",
    "Tit": "تي",
    "Phm": "فل",
    "Heb": "عب",
    "Jas": "يع",
    "1Pe": "١ بط",
    "2Pe": "٢ بط",
    "1Jn": "١ يو",
    "2Jn": "٢ يو",
    "3Jn": "٣ يو",
    "Jud": "يه",
    "Re": "رؤ"
}
books_model = {"id": "recIFusdNl6d8dj3L",
               "fields": {
                   "osisName": "Gen",
                   "bookName": "Genesis",
                   "bookName_ar": "التكوين",
                   "bookDiv": "Pentateuch",
                   "bookDiv_ar": "\u0627\u0644\u0634\u0631\u064a\u0639\u0629",
                   "testament": "Old Testament",
                   "testament_ar": "\u0627\u0644\u0639\u0647\u062f \u0627\u0644\u0642\u062f\u064a\u0645",
                   "shortName": "Ge",
                   "shortName_ar": "تك",
                   "bookOrder": 1,
                   "verses": [],
                   "verses_os": [],
                   "chapters": [],
                   "chapters_os": [],
                   "chapterCount": 50,
                   "verseCount": 1533,
                   "writers": ["moses_2108"],
                   "slug": "gen",
                   "peopleCount": 1082,
                   "writers_id": ["recjNRR60PAuFtjha"],
                   "placeCount": 266
               },
               "createdTime": "2018-05-13T17:19:17.000Z"
               }
books_model_list = list(books_model['fields'].keys())
print(books_model_list)

with open('../people/people.json') as people_json_file:
    people = json.load(people_json_file)


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
            elif key == "bookName_ar":
                bookName = item['fields']['bookName']
                new_item['fields'][key] = arabic_books[bookName]
                # print(bookName)
            elif key == "bookDiv_ar":
                bookDiv = item['fields']["bookDiv"]
                new_item['fields'][key] = arabic_divisions[bookDiv]
                # print(bookDiv)
            elif key == "testament_ar":
                testament = item['fields']["testament"]
                new_item['fields'][key] = arabic_testaments[testament]
                # print(testament)
            elif key == "shortName_ar":
                shortName = item['fields']["shortName"]
                new_item['fields'][key] = arabic_shortName[shortName]
                # print(shortName)
            elif key == "verses_os":
                # osis_verses
                verses = item["fields"]['verses']
                osisRefV = []
                with open('../verses/verses.json') as verses_json_file:
                    verses_id_changing = json.load(verses_json_file)
                    for verse_str_id in verses:
                        for ver_os in verses_id_changing:
                            if ver_os['id'] == verse_str_id:
                                osisRefV.append(ver_os['fields']['osisRef'])
                new_item['fields']['verses_os'] = osisRefV
            elif key == "chapters_os":
                # osis_chapters
                chapters = item['fields']['chapters']
                print(len(chapters))
                oisisRefChapters = []
                with open('../chapters/chapters.json') as verses_json_file:
                    chapters_id_changing = json.load(verses_json_file)
                    print(len(chapters_id_changing))
                    for chapter_str_id in chapters:
                        # print(chapter_str_id)
                        for chapter_os in chapters_id_changing:
                            if chapter_os['id'] == chapter_str_id:
                                oisisRefChapters.append(
                                    chapter_os['fields']['osisRef'])
                new_item['fields']['chapters_os'] = oisisRefChapters
            elif key == "writers_id":
                # fixing the writers from a string to search to the id of the person in people.json
                writers = item["fields"]["writers"]
                item["fields"]["writers_id"] = []
                new_writers = []
                for writer in writers:
                    for person in people:
                        if writer == person["fields"]["personLookup"]:
                            writer_new_id = person["id"]
                            new_writers.append(writer_new_id)
                new_item["fields"]["writers_id"] = new_writers

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
