from googletrans import Translator
source_text = """
text
"""
translator = Translator()
res = translator.translate(source_text, dest='ar')
print(res)