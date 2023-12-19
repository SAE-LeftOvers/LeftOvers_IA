from typing import List
import json

from connection import Connection
from business_classes import Ingredient, Recipe, IngredientsClasses

class RecipesService:
    def __init__(self):
        self.connection = Connection()
    
    def get_available_recipes_with_ingredients(self, ingredients_ids: List[int]):
        params = ''
        for id in ingredients_ids:
            params = params + str(id) + ':'
        if (len(params) > 0):
            params = params[:-1]

        results = self.connection.ask(path='/recipes/withingr/', params=params)
        if (results == None):
            return None
        
        try:
            recipes_data = json.loads(results)
            recipes = []
            for recipe_data in recipes_data:
                ingredients = [Ingredient(ingr['id'], ingr['name']) for ingr in recipe_data['ingredients']]
                comments_dictionary = self.__get_comments_dico(recipe_data['id'])
                rating_list = self.__get_rating_list(recipe_data['id'])
                recipe = Recipe(
                    recipe_data['id'], 
                    recipe_data['name'], 
                    recipe_data['description'], 
                    recipe_data['time_to_cook'], 
                    recipe_data['steps'], 
                    ingredients, 
                    comments_dictionary,
                    rating_list)
                recipes.append(recipe)
        
            return recipes
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def __get_comments_dico(self, recipe_id: int):
        try:
            results = self.connection.ask('/recipes/getcommentsdictionary/', params=recipe_id)

            comments_data = json.loads(results)

            return comments_data

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def __get_rating_list(self, recipe_id: int):
        try:
            results = self.connection.ask('/recipes/getratinglist/', params=recipe_id)

            rating_data = json.loads(results)

            return rating_data

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    
    def __get_recipe_respected_filters(self, recipe_id: int):
        try:
            results = self.connection.ask('/class/ofrecipe/', params=recipe_id)

            respected_filters_strings = json.loads(results)

            respected_filters_enums = [IngredientsClasses[item] for item in respected_filters_strings]

            print("recipe id :", recipe_id, ", respected filters :", respected_filters_enums)

            return respected_filters_enums

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []
    
    def get_available_recipes_with_ingredients_and_filters(self, ingredients_ids: List[int], filters: List[IngredientsClasses]):
        if not filters:
            return self.get_available_recipes_with_ingredients(ingredients_ids=ingredients_ids)

        available_recipes_before_filter = self.get_available_recipes_with_ingredients(ingredients_ids=ingredients_ids)
        final_recipes = []

        for recipe in available_recipes_before_filter:
            respected_filters = self.__get_recipe_respected_filters(recipe.id)

            # Vérifier si la recette contient des ingrédients non conformes aux filtres
            if any(filter_to_respect not in respected_filters for filter_to_respect in filters):
                continue

            final_recipes.append(recipe)

        return final_recipes

