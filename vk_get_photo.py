import requests
import json
import io
from pprint import pprint

with open('privat/token.txt', 'r') as vk_token:
    token = vk_token.readline().strip()

def write_json(data):
    with io.open('photos.json', 'w', encoding="utf-8", errors="ignore") as vk_response:
        json.dump(data, vk_response, indent=2, ensure_ascii=False)

def result_json(photo_list):
    with open('result.json', 'w', encoding="utf-8") as result_json_file:
        json.dump(photo_list, result_json_file, indent=2, ensure_ascii=False)

def get_largest(size_dict):
    weight = {'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 'm' : 10, 'x' : 20, 'y' : 30, 'z' : 40, 'w' : 50}
    size_dict['type'] = weight[size_dict['type']]
    return size_dict['type']

def vk_get_photo():
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': 1781716,
        'access_token': token,
        'album_id': 'profile',
        'photo_sizes': 1,
        'count': 5,
        'extended': 1,
        'v': 5.131,
    }

    res = requests.get(URL, params=params)
    write_json(res.json())

    photos = json.load(open('photos.json'))['response']['items']
    photo_list = []
    for photo in photos:
        photo_inf = {}

        photo_inf['name'] = str(photo['likes']['count']) + '.jpeg'
        
        sizes = photo['sizes']
        max_sizes_url = max(sizes, key=get_largest)['url']
        photo_inf['url'] = max_sizes_url

        photo_list.append(photo_inf)
        
    result_json(photo_list.json())

        
        

if __name__ == '__main__':
    vk_get_photo()