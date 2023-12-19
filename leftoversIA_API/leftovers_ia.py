from typing import List

from services import RecipesService
from DictionaryAnalyzer import DictionaryAnalyzer
from business_classes import Recipe, Ingredient, IngredientsClasses
from utils import get_insert_rg

class LeftoversIA:
    def __init__(self):
        self.service = RecipesService()
        self.dictionary_analyzer = DictionaryAnalyzer()
        self.review_wordspoints_attribution = {'bad':2, 'ok':3, 'basic': 3, 'happy': 4, 'like': 4, 'love': 5, 'good': 5, 'yum': 6, 'yummy': 6, 'tasty':7, 'excellent': 8, 'wonderful': 8, 'delicious': 8}
        self.quickness_wordspoints_attribution = {'consuming': 1, 'slow': 3, 'average': 7, 'quick': 9}
        self.difficulty_wordspoints_attribution = {'desperate': 1, 'hard': 2, 'work': 2, 'wrong': 2, 'practice': 3, 'average': 5, 'easy': 7, 'clear':7}
        self.type_wordspoints_attribution = {'family': 4, 'traditionnal': 5, 'modern': 6}
    
    def use_ai(self, ingredient_ids: List[int], filters_to_respects: List[IngredientsClasses] = []):
        if (len(filters_to_respects) >= 1):
            recipes = self.service.get_available_recipes_with_ingredients_and_filters(ingredients_ids=ingredient_ids, filters=filters_to_respects)
        else:
            recipes = self.service.get_available_recipes_with_ingredients(ingredients_ids=ingredient_ids)
        
        if ((recipes == None) or (recipes == [])) :
            return None

        evaluation = self.__evaluate_several_recipes(recipes)
        
        return evaluation["ordered_recipes"]
    
    def __evaluate_one_recipe(self, recipe: Recipe):
        # note = recipe.ttc/60*100 + len(recipe.ingredients)*100
        note = 0
        review_note = self.dictionary_analyzer.analyze(self.review_wordspoints_attribution, recipe.comments_dictionary)
        quickness_note = self.dictionary_analyzer.analyze(self.quickness_wordspoints_attribution, recipe.comments_dictionary)
        difficulty_note = self.dictionary_analyzer.analyze(self.difficulty_wordspoints_attribution, recipe.comments_dictionary)
        type_note = self.dictionary_analyzer.analyze(self.type_wordspoints_attribution, recipe.comments_dictionary)

        nb_reviews = len(recipe.rating_list)
        rating_mean = sum(recipe.rating_list)/(1 if nb_reviews == 0 else nb_reviews)
        mean_bonus = 0
        if (rating_mean>=4):
            bonus = 3
        elif (rating_mean >= 3):
            bonus = 2
        elif (rating_mean>=2):
            bonus = 1
        
        review_quantity_bonus = 0
        if (nb_reviews >= 10):
            review_quantity_bonus = 5
        elif (nb_reviews >= 7):
            review_quantity_bonus = 3
        elif (nb_reviews >= 3):
            review_quantity_bonus = 1

        note = (review_note + quickness_note + difficulty_note + type_note) / 4 + mean_bonus + review_quantity_bonus

        print(f'recipe_id={recipe.id}, recipe_note={note}')
        return note
    
    def __evaluate_several_recipes(self, recipes: List[Recipe]):
        output_data = {
            "ordered_recipes": [],
            "notes": []
        }

        for recipe in recipes:
            note = self.__evaluate_one_recipe(recipe)
            i = get_insert_rg(output_data["notes"], note)
            output_data["ordered_recipes"].insert(i, recipe)
            output_data["notes"].insert(i, note)

        print("final order =", output_data["notes"])
        
        return output_data
