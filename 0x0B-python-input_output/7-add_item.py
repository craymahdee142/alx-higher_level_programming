#!/usr/bin/python3
'''Add all aurguments to Python list and save it to a file'''

import sys
import os
import os.path

save_to_json_file = __import__("save_to_json_file.py").save_to_json_file
load_from_json_file =  __import__ ("load_from_jdon_file.py")load_from_json_file


items = "add_item.json"
if os.path.isfile(items):
    obj = load_from_json_file(items)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, items)
