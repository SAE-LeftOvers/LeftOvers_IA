from flask import Flask, Response
from flask_cors import CORS

from leftovers_ia import LeftoversIA
from utils import convert_obj_to_json
from business_classes import Recipe, IngredientsClasses

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "methods": "GET"}})


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getrecipes/<string:ingr_ids>')
def get_recipes(ingr_ids):
    ingr_ids_list = [int(raw_id) for raw_id in ingr_ids.split(':')]

    ia = LeftoversIA()
    recipes = ia.use_ai(ingr_ids_list)
    if (recipes == None):
        rawlist = []
        rawlist.append(Recipe(-1, 'No such recipe', 'No such recipe', 0, ['no such recipe'], [], {}, []))
        json_data = convert_obj_to_json(rawlist)
        return Response(json_data, content_type='application/json')

    json_data = convert_obj_to_json(recipes)
    response = Response(json_data, content_type='application/json')

    return response

@app.route('/getrecipeswithfilters/<string:ingr_ids>/<string:filters>')
def get_recipes_with_filters(ingr_ids, filters):
    ingr_ids_list = [int(raw_id) for raw_id in ingr_ids.split(':')]
    filters_to_respect = []
    for filter_name in filters.split(':'):
        try:
            filter_enum = IngredientsClasses[filter_name]
            filters_to_respect.append(filter_enum)
        except KeyError:
            error_message = f"Le filtre {filter_name} n'est pas valide."
            return Response(error_message, status=400, content_type='text/plain')
    
    print(filters_to_respect)
    
    ia = LeftoversIA()
    recipes = ia.use_ai(ingr_ids_list, filters_to_respect)
    if (recipes == None):
        rawlist = []
        rawlist.append(Recipe(-1, 'No such recipe', 'No such recipe', 0, ['no such recipe'], [], {}, []))
        json_data = convert_obj_to_json(rawlist)
        return Response(json_data, content_type='application/json')

    json_data = convert_obj_to_json(recipes)
    response = Response(json_data, content_type='application/json')

    return response

if __name__ == '__main__':
    app.run(debug=True)