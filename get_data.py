import requests
import json
import os.path

API = 'https://pokeapi.co/api/v2/pokemon/'
TARGET_DIR = "./poke-data/"
TARGET_FORMAT = ".json"


def store_data(data):
    json_data = json.loads(data)
    name = json_data["name"]
    target_file_path = TARGET_DIR + name + TARGET_FORMAT

    # Creates directory if it does not exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Will NOT overwrite file with the same name
    if not os.path.exists(target_file_path):
        f = open(target_file_path, "w+")
        f.write(data)
        f.close()


def get_data():
    # gets first generation of pokemon
    for i in range(1, 152):
        url = API + str(i)
        response = requests.request("GET", url)
        if i == 1:
            print(response.text)
        try:
            store_data(response.text)
        except json.decoder.JSONDecodeError:
            print("Service may be down")
            break


get_data()
