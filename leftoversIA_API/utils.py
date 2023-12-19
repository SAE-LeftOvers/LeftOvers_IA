import json
from typing import List

from business_classes import Ingredient, Recipe

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Ingredient, Recipe)):
            return obj.to_dict()
        return super(CustomJSONEncoder, self).default(obj)

def convert_obj_to_json(obj):
    return json.dumps(obj, cls=CustomJSONEncoder)

def get_insert_rg(notes: List[float], note_to_insert: float):
    i = 0
    while (i < len(notes)) and (note_to_insert < notes[i]):
        i+=1
    return i