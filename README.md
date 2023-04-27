L'objectif de ce TD est de partir d'une partie des développements réalisés dans le TD sur Docker et d'étendre cela à une API Rest.
Ceci n'est qu'une introduction aux API Rest et vous ne traiterez pas l'asynchronisme ni les aspects liés à la sécurité / authentification / autorisation.

# Exercice 1 - API Rest avec FastAPI

Faites une API Rest avec FASTAPI qui accède à une base de donnée mongodb afin de fournir les endpoits suivants :

- [GET] eggs
- [POST] eggs
- [GET] eggs/immatriculation
- [DELETE] eggs/immatriculation
- [UPDATE] eggs/immatriculation

Le modèle utilisé, nommé `ModelEgg`, doit être composé d'un `élevage` (origine de l'oeuf), d'une `couleur` (gris, brun, blanc) et d'une `immatriculation` (cf. TD Docker). Dans le cas de l'endpoint `[POST] eggs`, assurez vous qu'une `HTTPException` soit retournée lorsque l'immatriculation fournie est déjà enregistrée.

**Indications** : vous utiliserez deux conteneurs, le premier remplira une base de donnée (cf. TD Docker), le second exposera l'API Rest sur le port 3000. Il est attendu que votre modèle soit défini dans un fichier `model_egg.py`, que votre application RestAPI soit définie dans un fichier `app.py`, et que la logique associée au parsing d'immatriculation soit contenue dans un fichier `immat_parser.py`.

**Note** : utilisez des `validator` pour vous assurer que l'immatriculation et la couleur du modèle sont valides (https://pydantic-docs.helpmanual.io/usage/validators/).

# Exercice 2 - Paramétrisation

Retravaillez l'endpoint `[GET] eggs/immatriculation` pour qu'il affiche plus d'informations. Celui-ci devra permettre d'afficher (si spécifié) les informations suivantes :

- numéro d'identification de l'oeuf;
- le poids de l'oeuf;
- le pays d'origine de l'oeuf;
- le jour de ponte;
- le mois de ponte.

Etendez l'endpoint `[POST] eggs` pour que celui-ci n'accepte que des oeufs de poids supérieur à 60g qui ne sont pas pondus un jour pair.

# Exercice 3 - Livraison

Rédigez un docker compose permettant de lancer le tout.

# Exercice 4 - Changement de backend

Modifiez votre API pour que celle-ci fonctionne avec un stockage des données basé sur un fichier json et non plus une base de données. Pour vous aider, vous pourriez utiliser les appels suivant :

```python
import json

def read_json(json_path):
  with open(json_path, "r") as f:
    return json.loads(f.read())

def write_json(json_path, data):
  with open(json_path, "w") as f:
    json.dupmp(data, f, indent=4)
```

Modifiez votre docker compose pour pouvoir livrer votre nouvelle version


