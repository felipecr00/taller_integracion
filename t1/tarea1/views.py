from django.shortcuts import render
import requests

# Aqui dejare los consumos de la API

def generate_request(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


def get_episodes(url, params={}):
    response = generate_request(url, params)
    if response:
        user = response.get('results')
        return user
    return ''


def get_info(url, params={}):
    response = generate_request(url, params)
    if response:
        # info = response.get()
        return response
    return ''

## Llamadas a la API
episodios_1 = get_episodes('https://rickandmortyapi.com/api/episode?page=1')
episodios_2 = get_episodes('https://rickandmortyapi.com/api/episode?page=2')

list_complete_episodes = episodios_1 + episodios_2
lista_named_epis = []
for info in list_complete_episodes:
    lista_named_epis.append([info["id"], info["name"], info["air_date"], info["episode"]])

# Funciones de las vistas
def home(request):
    return render(request, "home.html", {"episodios": lista_named_epis})


def listado_episodios(request):
    return render(request, "table.html", {"episodios": lista_named_epis, "prueba": "logrado"})


def info_episodio(request, id):
    info = get_info(f'https://rickandmortyapi.com/api/episode/{id}')

    name = info["name"]
    air_date = info["air_date"]
    episode = info["episode"]
    characters = info["characters"]
    lista_characters = []
    lista_name_characters = []

    # Obtengo la lista de characters del episodio con url, extraigo el id
    for li in characters:
        ch_id = li.split('/')[-1]
        lista_characters.append(ch_id)

    chars_interes = ",".join(map(str, lista_characters))


    # realizo request con los datos de todos los ids
    info_chars = get_info(f'https://rickandmortyapi.com/api/character/{chars_interes}')

    for ic in info_chars:
        lista_name_characters.append(ic["name"])

    final_list = list(map(list, zip(lista_name_characters, lista_characters)))

    return render(request, "episode.html", {"name": name,
                                            "air_date": air_date,
                                            "episode": episode,
                                            "characters": final_list})

def character(request, id):
    info = get_info(f'https://rickandmortyapi.com/api/character/{id}')
    name =info["name"]
    status =info["status"]
    species = info["species"]
    type = info["type"]
    gender = info["gender"]
    origin = info["origin"]
    location = info["location"]
    image = info["image"]
    #print(name)
    lista_episodios = []
    lista_name_eps = []

    # Aqui rescatamos los links asociados a lso episodios
    episodes = info["episode"]
    for ep in episodes:
        ep_id = ep.split('/')[-1]
        lista_episodios.append(int(ep_id))
    eps_interes = ",".join(map(str, lista_episodios))

    # realizo request con los datos de todos los ids
    info_eps = get_info(f'https://rickandmortyapi.com/api/episode/{eps_interes}')

    if info_eps.__class__ is  dict:
        lista_name_eps.append(info_eps["name"])
    else:
        for ie in info_eps:
            lista_name_eps.append(ie["name"])

    final_list = list(map(list, zip(lista_name_eps, lista_episodios)))

    return render(request, "character.html", { "name" : name,
                                             "status": status,
                                             "species": species,
                                             "type": type,
                                             "gender": gender,
                                             "origin": [origin["name"],origin["url"].split('/')[-1]],
                                             "location": [location["name"],location["url"].split('/')[-1]],
                                             "episodes" : final_list,
                                             "image": image})


def lugar(request, id):
    info = get_info(f'https://rickandmortyapi.com/api/location/{id}')
    name = info["name"]
    type = info["type"]
    dimension = info["dimension"]
    residents = info["residents"]
    lista_name_residents = []

    lista_re_id = []

    for r in residents:
        lista_re_id.append(r.split("/")[-1])
    re_interes = ",".join(map(str, lista_re_id))

    info_chars = get_info(f'https://rickandmortyapi.com/api/character/{re_interes}')

    for c in info_chars:
        lista_name_residents.append(c["name"])

    final_list = list(map(list, zip(lista_name_residents, lista_re_id)))


    return render(request, "location.html", {"name": name, "dimension": dimension, "type": type, "residents": final_list})

