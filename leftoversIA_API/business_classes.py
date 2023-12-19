from typing import List, Dict
from enum import Enum

class Ingredient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def to_dict(self):
        return { 'id': self.id, 'name': self.name }

class Recipe:
    def __init__(self, id: int, name: str, desc: str, ttc: int, steps: List[str], ingredients: List[Ingredient], comments_dictionary: Dict[str, int], rating_list: List[int]):
        self.id = id
        self.name = name
        self.desc = desc
        self.ttc = ttc
        self.steps = steps
        self.ingredients = ingredients
        self.comments_dictionary = comments_dictionary
        self.rating_list = rating_list
    
    def __str__(self):
        ingr_list_str = '['
        for ingr in self.ingredients:
            ingr_list_str += str(ingr)+', '
        if (len(ingr_list_str) > 0):
            ingr_list_str = ingr_list_str[:-2]
        ingr_list_str += ']'
        return f"{self.name} (id={self.id}, desc={self.desc}, ttc={self.ttc}, ingr={ingr_list_str})"
    
    def to_dict(self):
        ingredient_list_json = []
        for ingr in self.ingredients:
            ingredient_list_json.append(ingr.to_dict())
        return {'id': self.id, 'name': self.name, 'description': self.desc, 'time_to_cook': self.ttc, 'steps': self.steps, 'ingredients': ingredient_list_json}

class IngredientsClasses(Enum):
    DAIRY_FREE = 'DAIRY_FREE'
    GLUTEN_FREE = 'GLUTEN_FREE'
    PORCLESS = 'PORCLESS'
    VEGAN = 'VEGAN'
    VEGETARIAN = 'VEGETARIAN'
    PESCATARIAN = 'PESCATARIAN'
