from dotenv import load_dotenv
import os
import requests as rq

load_dotenv()

class Connection:
    base_url: str = ''
    headers_base = {"Content-Type": "application/json"}

    def __init__(self):
        self.base_url = os.getenv("API_BASEURL")
    
    def ask(self, path: str, params: str):
        if (len(path) > 0):
            if (path[0] == '/'):
                path = path[1:]
            if (path[-1] == '/'):
                path = path[:-1]
        if ((params is str) and (len(params) > 0) and (params[0] == '/')):
            params = params[1:]
        response = rq.get(self.base_url+path+'/'+str(params), headers=self.headers_base)

        if response.status_code == 200:
            return response.content
        elif response.status_code == 404:
            return None
        else:
            print(f"Erreur lors de la requête. Code de statut : {response.status_code}")
            print(response.text)
            return None