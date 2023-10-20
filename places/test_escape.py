import json
import codecs

def escape_arabic_unicode(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    def escape_unicode(value):
        if isinstance(value, str):
            return codecs.decode(value, 'unicode_escape')
        elif isinstance(value, list):
            return [escape_unicode(item) for item in value]
        elif isinstance(value, dict):
            return {key: escape_unicode(val) for key, val in value.items()}
        else:
            return value
    
    escaped_data = escape_unicode(data)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(escaped_data, file, ensure_ascii=False, indent=4)

# Usage example:
input_file = 'places/places_united_schema.json'
output_file = 'data_escaped.json'
escape_arabic_unicode(input_file, output_file)
print("Escaping Arabic Unicode complete. The updated data is written to", output_file)
