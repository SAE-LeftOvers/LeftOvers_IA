# LeftOvers_IA

L'Ia de LeftOvers permet la suggestion de recette à partir d'une liste d'ingrédient et de critère.

## Version avec API
Vous pouvez essayer l'IA en local se plaçant dans le répertoire **leftoversIA_API**.

### Prérequis

* python3
* pip
* librairies/modules python :
  * os
  * python-dotenv
  * typing
  * requests
  * json
  * flask
* Créez un .env : vous devez y définir la variable d'environnement **API_BASEURL** qui doit contenir l'adresse ou contacter l'API.

### Utilisation
Entrez ```python3 app.py``` dans un terminal en étant dans le dossier **leftoversIA_API**. Vous devriez obtenir un visuel de ce format :
```
 > python3 app.py 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 198-826-709
```
Si oui, ouvrez un navigateur est testez l'adresse *http://127.0.0.1:5000* ou cliquez sur le lien directement dans le terminal.  
Vous devriez simplement voir apparaître **Hello, World!** dans le navigateur. Sinon, vérifier l'installation des modules python.  

Ensuite, vous pouvez essayer les liens suivants :
 * http://127.0.0.1:5000/getrecipes/1928:2148:2809:2853:3723:6261:6335:7076
 * http://127.0.0.1:5000/getrecipes/389:7655:6270:1527:3406:2683:4969:800:5298:840:2499:6632:7022:1511:3248:4964

Vous devriez obtenir les résultats respectifs suivants :
 * 1 résultat avec pour id -> 4444
 * 19 résultats avec pour ids -> 146223, 137357, 424415, ...

### Evolution

![an image should shows up](/ExpositionImages/ai_evolution_sample.jpg "Exemple d'évolution du système de notation")
 
